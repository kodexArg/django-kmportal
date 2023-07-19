from loguru import logger
import secrets
from datetime import timedelta
from django.db import models
from django.db.models import Case, When, Value, IntegerField, Manager
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from django.db.models import Case, When, Value, IntegerField
from django.utils.timezone import now
from django.utils.translation import gettext as _


# Create your models here.
class Setting(models.Model):
    """This table is using for this project settings, some important values are:
    domain: the domain of the project
    ... (todo)
    """

    name = models.CharField(max_length=30, unique=True)
    value = models.TextField()

    def __str__(self):
        return self.name


class PumpOperators(models.Model):
    """This table is using for the pump operator's login

    To create a new user use the proposed_email method:

    user = User.objects.create_user(
        'XXXXXXXX', proposed_email, 'password'
        )user = User.objects.create_user('username', proposed_email, 'password')

    pump_operator = PumpOperators.objects.create(
        user=user, short_name='ShortName'
        )
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=50, unique=True)

    @classmethod
    def proposed_email(cls, first_name, last_name):
        # Retrieve the domain from the Setting model
        try:
            domain = Setting.objects.get(name="domain").value
        except ObjectDoesNotExist:
            domain = "mycompany.com"

        email = f"{first_name}.{last_name}@{domain}"
        return email

    def __str__(self):
        return self.short_name


class Company(models.Model):
    """B2B Partner Company"""

    name = models.CharField(max_length=255)
    fantasy_name = models.CharField(max_length=255)
    cuit = models.IntegerField(unique=True)

    def __str__(self):
        return self.fantasy_name

    class Meta:
        verbose_name_plural = _("Companies")


class CompanySocialAccount(models.Model):
    """This model creates a one-to-one relation with SocialAccount
    and a foreign key relation with Company.
    A social account can have one Company assigned to it (or none, as
    indicated by null=True, blank=True)."""

    social_account = models.OneToOneField(SocialAccount, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.social_account.extra_data['name']} → {self.company}"


class Drivers(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name=_("first_name"))
    last_name = models.CharField(max_length=255, verbose_name=_("last_name"))
    identification_type = models.CharField(max_length=50, default=_("identification_type"))
    identification_number = models.CharField(max_length=50, verbose_name=_("identification_number"))
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tractors(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    domain = models.CharField(max_length=15, verbose_name=_("domain"))
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.domain = self.domain.upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.domain


class Trailers(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    domain = models.CharField(max_length=15, verbose_name=_("domain"))
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.domain = self.domain.upper()
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.domain


class FuelOrdersManager(Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                custom_sort_order=Case(
                    When(
                        is_blocked=True,
                        is_canceled=False,
                        is_finished=False,
                        then=Value(1),
                    ),
                    When(is_canceled=False, is_finished=False, then=Value(2)),
                    When(is_canceled=True, then=Value(4)),
                    When(is_finished=True, then=Value(4)),
                    default=Value(3),
                    output_field=IntegerField(),
                )
            )
            .order_by("custom_sort_order", "-requested_date", "-id")
        )


class FuelOrders(models.Model):
    """Core Table of the refueling Workflow
    this models uses a custom manager FuelOrdersManager
    """

    objects = FuelOrdersManager()

    # Typo Comb choices
    FUEL_TYPE_CHOICES = [
        ("infinia_diesel", "Infinia Diesel"),
        ("infinia", "Infinia"),
        ("diesel_500", "Diesel 500"),
        ("super", "Super"),
    ]

    AGREEMENT_CHOICES = [
        (0, _("no_agreement")),
        (1, _("under_negotiation")),
        (2, _("agreed")),
    ]

    color_map = {
        "infinia_diesel": "#225722",
        "diesel_500": "#1453FF",
        "infinia": "#FF4500",
        "super": "#ffa500",
    }

    fuel_type_map = {
        "infinia_diesel": "Inf. D.",
        "infinia": "Infinia",
        "diesel_500": "D. 500",
        "super": "Super",
    }

    operation_code = models.CharField(max_length=6, unique=True, blank=True, null=True)

    order_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    requested_date = models.DateField(default=now)
    expiration_date = models.DateField(default=now() + timedelta(days=7))

    user_creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="fuel_orders_created",
        blank=True,
        null=True,
    )
    user_lastmod = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="fuel_orders_modified",
        blank=True,
        null=True,
    )

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    driver = models.ForeignKey(Drivers, on_delete=models.PROTECT)

    tractor_plate = models.ForeignKey(Tractors, on_delete=models.PROTECT, verbose_name="tractor_plate")
    trailer_plate = models.ForeignKey(
        Trailers,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name="trailer_plate",
    )

    tractor_fuel_type = models.CharField(
        max_length=50,
        choices=FUEL_TYPE_CHOICES,
        blank=True,
        null=True,
        verbose_name="tractor_fuel_type",
    )
    backpack_fuel_type = models.CharField(
        max_length=50,
        choices=FUEL_TYPE_CHOICES,
        blank=True,
        null=True,
        verbose_name="backpack_fuel_type",
    )
    chamber_fuel_type = models.CharField(
        max_length=50,
        choices=FUEL_TYPE_CHOICES,
        blank=True,
        null=True,
        verbose_name="chamber_fuel_type",
    )

    tractor_liters = models.PositiveIntegerField(blank=True, null=True, verbose_name="tractor_liters")  # leave blank until filled
    backpack_liters = models.PositiveIntegerField(blank=True, null=True, verbose_name="backpack_liters")  # leave blank until filled
    chamber_liters = models.PositiveIntegerField(blank=True, null=True, verbose_name="chamber_liters")  # leave blank until filled

    tractor_liters_to_load = models.IntegerField(default=0, verbose_name="tractor_liters_to_load")  # show MAX on -1 and NO on 0
    backpack_liters_to_load = models.IntegerField(default=0, verbose_name="backpack_liters_to_load")  # show MAX on -1 and NO on 0
    chamber_liters_to_load = models.IntegerField(default=0, verbose_name="chamber_liters_to_load")  # show MAX on -1 and NO on 0

    requires_odometer = models.BooleanField(default=False, verbose_name="requires_odometer")
    requires_kilometers = models.BooleanField(default=False, verbose_name="requires_kilometers")

    is_blocked = models.BooleanField(default=False, verbose_name="is_blocked")  # because it has been attended
    is_canceled = models.BooleanField(default=False, verbose_name="is_canceled")  # because there's an error or user action
    is_finished = models.BooleanField(default=False, verbose_name="is_finished")  # because it's been attended and it's been filled

    cancel_reason = models.TextField(blank=True, null=True, verbose_name="cancel_reason")  # because there's an error or user action

    AGREEMENT_CHOICES = [
        ("under_negotiation", "Under Negotiation"),
        ("no_agreement", "No Agreement"),
        ("agreed", "Agreed"),
    ]

    in_agreement = models.CharField(choices=AGREEMENT_CHOICES, default="under_negotiation", max_length=20, verbose_name="in_agreement")

    comments = models.TextField(blank=True, null=True, verbose_name="comments")

    def save(self, *args, **kwargs):
        """This save method accept some missing fields:
        ["requested_date", "expiration_date", "in_agreement"]
        """

        try:
            if not self.pk:  # this is a new record
                self.operation_code = secrets.token_hex(3)
                while FuelOrders.objects.filter(operation_code=self.operation_code).exists():
                    self.operation_code = secrets.token_hex(3)

                if hasattr(self, "user_creator") and self.user_creator is None:
                    self.user_creator = self._get_current_user()

                if hasattr(self, "company") and self.company is None:
                    self.company = self._get_user_company()

                if not self.requested_date:
                    self.requested_date = now()

                if not self.expiration_date:
                    self.expiration_date = now() + timedelta(days=7)

            else:  # this is an edition
                if hasattr(self, "user_lastmod"):
                    self.user_lastmod = self._get_current_user()
        except Exception as e:
            logger.error(f"Error on saving fuel order: {e}")

        super().save(*args, **kwargs)

    def get_total_liters(self):
        return self.tractor_liters + self.backpack_liters + self.chamber_liters

    def _get_current_user(self):
        # Get the current authenticated user using Django-Allauth
        try:
            social_account = SocialAccount.objects.get(user=self.request.user)
            return social_account.user
        except (AttributeError, SocialAccount.DoesNotExist):
            return None

    def _get_user_company(self):
        # Get the user's company based on the SocialAccount
        try:
            social_account = SocialAccount.objects.get(user=self.request.user)
            company_social_account = CompanySocialAccount.objects.get(social_account=social_account)
            return company_social_account.company
        except (
            AttributeError,
            SocialAccount.DoesNotExist,
            CompanySocialAccount.DoesNotExist,
        ):
            return None

    @property
    def short_tractor_fuel_type(self):
        return self.fuel_type_map.get(self.tractor_fuel_type, "")

    @property
    def tractor_fuel_type_color(self):
        return self.color_map.get(self.tractor_fuel_type, "")

    @property
    def short_backpack_fuel_type(self):
        return self.fuel_type_map.get(self.backpack_fuel_type, "")

    @property
    def backpack_fuel_type_color(self):
        return self.color_map.get(self.backpack_fuel_type, "")

    @property
    def short_chamber_fuel_type(self):
        return self.fuel_type_map.get(self.chamber_fuel_type, "")

    @property
    def chamber_fuel_type_color(self):
        return self.color_map.get(self.chamber_fuel_type, "")

    @property
    def formated_tractor_liters_to_load_of(self):
        if self.tractor_liters_to_load == 0:
            return "no"
        elif self.tractor_liters_to_load == -1:
            return "max"
        else:
            return f"{ self.tractor_liters_to_load } "

    @property
    def formated_backpack_liters_to_load_of(self):
        if self.backpack_liters_to_load == 0:
            return "no"
        elif self.backpack_liters_to_load == -1:
            return "max"
        else:
            return f"{ self.backpack_liters_to_load } "

    @property
    def formated_chamber_liters_to_load_of(self):
        if self.chamber_liters_to_load == 0:
            return "no"
        elif self.chamber_liters_to_load == -1:
            return "max"
        else:
            return f"{ self.chamber_liters_to_load } "

    def __str__(self):
        return self.operation_code

    class Meta:
        verbose_name = "Fuel Order"
        verbose_name_plural = "Fuel Orders"


class Refuelings(models.Model):
    """Core Table of the refueling Workflow: STEP 2"""

    ACCEPTANCE_STATUS_CHOICES = [
        (0, ""),
        (1, "Attending"),
        (2, "Finished"),
        (-1, "Canceled"),
    ]

    acceptance_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    fuel_order = models.ForeignKey(FuelOrders, on_delete=models.CASCADE)
    pump_operator = models.ForeignKey(PumpOperators, on_delete=models.CASCADE)
    status = models.IntegerField(choices=ACCEPTANCE_STATUS_CHOICES, default=0)
    tractor_pic = models.ImageField(upload_to="operation_code/tractor")
    backpack_pic = models.ImageField(upload_to="operation_code/backpack")
    chamber_pic = models.ImageField(upload_to="operation_code/chamber")
    tractor_liters = models.PositiveIntegerField(default=0)
    backpack_liters = models.PositiveIntegerField(default=0)
    chamber_liters = models.PositiveIntegerField(default=0)
    tractor_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES)
    backpack_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES)
    chamber_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES)
    odometer = models.PositiveIntegerField(null=True, blank=True)
    kilometers = models.PositiveIntegerField(null=True, blank=True)
    dispatch_note_pic = models.ImageField(upload_to="operation_code/dispatch_note")
    observation_pic = models.ImageField(upload_to="operation_code/others", null=True, blank=True)
    observation = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return str(self.fuel_order.operation_code)

    def get_total_liters(self):
        return self.tractor_liters + self.backpack_liters + self.chamber_liters


class ExtraCashManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                custom_sort_order=Case(
                    When(
                        is_blocked=True,
                        is_canceled=False,
                        is_finished=False,
                        then=Value(1),
                    ),
                    When(is_canceled=False, is_finished=False, then=Value(2)),
                    When(is_canceled=True, then=Value(4)),
                    When(is_finished=True, then=Value(4)),
                    default=Value(3),
                    output_field=IntegerField(),
                )
            )
            .order_by("custom_sort_order", "-requested_date", "-id")
        )


class ExtraCash(models.Model):
    """New model for the ExtraCash service"""

    objects = ExtraCashManager()

    AGREEMENT_CHOICES = [
        ("under_negotiation", "Under Negotiation"),
        ("no_agreement", "No Agreement"),
        ("agreed", "Agreed"),
    ]

    operation_code = models.CharField(max_length=6, unique=True, blank=True, null=True)

    order_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    requested_date = models.DateField(default=now)
    expiration_date = models.DateField(default=now() + timedelta(days=7))

    user_creator = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="extracash_created",
        blank=True,
        null=True,
    )
    user_lastmod = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name="extracash_modified",
        blank=True,
        null=True,
    )

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    driver = models.ForeignKey(Drivers, on_delete=models.PROTECT)

    is_blocked = models.BooleanField(default=False, verbose_name="is_blocked")
    is_canceled = models.BooleanField(default=False, verbose_name="is_canceled")
    is_finished = models.BooleanField(default=False, verbose_name="is_finished")

    cancel_reason = models.TextField(blank=True, null=True, verbose_name="cancel_reason")
    in_agreement = models.CharField(choices=AGREEMENT_CHOICES, default="under_negotiation", max_length=20, verbose_name="in_agreement")
    comments = models.TextField(blank=True, null=True, verbose_name="comments")

    cash_amount = models.PositiveIntegerField(verbose_name="cash_amount")

    def save(self, *args, **kwargs):
        try:
            if not self.pk:  # this is a new record
                self.operation_code = secrets.token_hex(3)
                while ExtraCash.objects.filter(operation_code=self.operation_code).exists():
                    self.operation_code = secrets.token_hex(3)

                if hasattr(self, "user_creator") and self.user_creator is None:
                    self.user_creator = self._get_current_user()

            else:  # this is an edition
                if hasattr(self, "user_lastmod"):
                    self.user_lastmod = self._get_current_user()
        except Exception as e:
            logger.error(f"Error on saving cash order: {e}")

        super().save(*args, **kwargs)

    def __str__(self):
        return self.operation_code

    class Meta:
        verbose_name = "ExtraCash Order"
        verbose_name_plural = "ExtraCash Orders"
