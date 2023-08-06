import secrets
from datetime import timedelta

from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Case, IntegerField, Manager, Value, When
from django.forms import ValidationError
from django.utils.timezone import now
from django.utils.translation import gettext as _
from loguru import logger


def get_default_expiration_date():
    return now() + timedelta(days=7)


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


class ExtraCashManager(models.Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                custom_sort_order=Case(
                    When(
                        is_locked=True,
                        is_paused=False,
                        is_finished=False,
                        then=Value(1),
                    ),
                    When(is_paused=False, is_finished=False, then=Value(2)),
                    When(is_paused=True, then=Value(4)),
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
    expiration_date = models.DateField(default=get_default_expiration_date)

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

    is_locked = models.BooleanField(default=False, verbose_name="is_locked")
    is_paused = models.BooleanField(default=False, verbose_name="is_paused")
    is_finished = models.BooleanField(default=False, verbose_name="is_finished")

    pause_reason = models.TextField(blank=True, null=True, verbose_name="pause_reason")
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

                if hasattr(self, "company") and self.company is None:
                    self.company = self._get_user_company()

                if not self.requested_date:
                    self.requested_date = now()

                if not self.expiration_date:
                    self.expiration_date = now() + timedelta(days=2)

            else:  # this is an edition
                if hasattr(self, "user_lastmod"):
                    self.user_lastmod = self._get_current_user()
        except Exception as e:
            logger.error(f"Error on saving cash order: {e}")

        super().save(*args, **kwargs)

    def _get_current_user(self):
        # Get the current authenticated user using Django-Allauth
        try:
            social_account = SocialAccount.objects.get(user=self.request.user)
            return social_account.user
        except (AttributeError, SocialAccount.DoesNotExist):
            return None

    def __str__(self):
        return self.operation_code if self.operation_code else "Unsaved FuelOrder"

    class Meta:
        verbose_name = "ExtraCash Order"
        verbose_name_plural = "ExtraCash Orders"


class FuelOrdersManager(Manager):
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .annotate(
                custom_sort_order=Case(
                    When(is_locked=True, is_paused=False, is_finished=False, then=Value(1)),
                    When(is_paused=False, is_finished=False, then=Value(2)),
                    When(is_paused=True, then=Value(4)),
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
        ("no_agreement", _("no_agreement")),
        ("under_negotiation", _("under_negotiation")),
        ("agreed", _("agreed")),
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
    expiration_date = models.DateField(default=get_default_expiration_date)

    user_creator = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="fuel_orders_created",
    )
    user_lastmod = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name="fuel_orders_modified",
    )

    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    driver = models.ForeignKey(Drivers, on_delete=models.PROTECT)

    tractor_plate = models.ForeignKey(Tractors, on_delete=models.PROTECT, verbose_name="tractor_plate")
    trailer_plate = models.ForeignKey(Trailers, on_delete=models.PROTECT, blank=True, null=True, verbose_name="trailer_plate")

    tractor_fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES, blank=True, null=True, verbose_name="tractor_fuel_type")

    backpack_fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES, blank=True, null=True, verbose_name="backpack_fuel_type")

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

    is_locked = models.BooleanField(default=False, verbose_name="is_locked")  # because its being attended
    is_paused = models.BooleanField(default=False, verbose_name="is_paused")  # because there's an error or user action
    is_finished = models.BooleanField(default=False, verbose_name="is_finished")  # because it's been attended and it's been filled

    in_agreement = models.CharField(choices=AGREEMENT_CHOICES, default="under_negotiation", max_length=20, verbose_name="in_agreement")
    comments = models.TextField(blank=True, null=True, verbose_name="comments")


    def clean(self):
        # Rule 1: if x_liters_to_load is non-zero, x_fuel_type is required.
        if self.tractor_liters_to_load != 0 and not self.tractor_fuel_type:
            raise ValidationError({'tractor_fuel_type': "Tractor fuel type is required if tractor liters to load is non-zero."})

        if self.backpack_liters_to_load != 0 and not self.backpack_fuel_type:
            raise ValidationError({'backpack_fuel_type': "Backpack fuel type is required if backpack liters to load is non-zero."})

        if self.chamber_liters_to_load != 0 and not self.chamber_fuel_type:
            raise ValidationError({'chamber_fuel_type': "Chamber fuel type is required if chamber liters to load is non-zero."})

        # Rule 2: if in_agreement changes to "agreed", disallow any further modification
        if self.pk:  # check if this instance is already saved in the database
            old_instance = FuelOrders.objects.get(pk=self.pk)  # retrieve the old instance
            if old_instance.in_agreement == "agreed" and self.in_agreement != "agreed":
                raise ValidationError({'in_agreement': "You cannot modify this order as it has already been approved. Please contact the administrator for further assistance."})

        # Rule 3: At least one of the tanks must be non-zero
        if all(x == 0 for x in [self.tractor_liters_to_load, self.chamber_liters_to_load, self.backpack_liters_to_load]):
            raise ValidationError("At least one of the tanks must be non-zero")

        # Always return the full collection of cleaned data.
        super().clean()


    def save(self, *args, **kwargs):
        # on new record, generate operation_code before saving the record
        if not self.pk:
            self.operation_code = secrets.token_hex(3)
            while FuelOrders.objects.filter(operation_code=self.operation_code).exists():
                self.operation_code = secrets.token_hex(3)
        logger.info(f"FuelOrders.save: {self.operation_code}")
        logger.debug(f"by {self.user_lastmod} company {self.company}")
        super().save(*args, **kwargs)

    def get_total_liters(self):
        return self.tractor_liters + self.backpack_liters + self.chamber_liters

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


