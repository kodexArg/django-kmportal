import secrets
from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


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


class Drivers(models.Model):
    LANGUAGES = [
        ("spanish", "Spanish"),
        ("english", "English"),
        ("portuguese", "Portuguese"),
    ]

    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    language = models.CharField(max_length=10, choices=LANGUAGES, default="english")
    identification_type = models.CharField(max_length=50)
    identification_number = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tractors(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.domain


class Trailers(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.domain


class FuelOrders(models.Model):
    """Core Table of the refueling Workflow: STEP 1"""

    # Typo Comb choices
    FUEL_TYPE_CHOICES = [
        ("infinia_diesel", "Infinia Diesel"),
        ("infinia", "Infinia"),
        ("diesel_500", "Diesel 500"),
        ("super", "Super"),
    ]

    AGREEMENT_CHOICES = [
        (0, "No agreement"),
        (1, "Under negotiation"),
        (2, "Agreed"),
    ]

    order_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    requested_date = models.DateField()
    operation_code = models.CharField(max_length=6, unique=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    expiration_date = models.DateField()
    driver = models.ForeignKey(Drivers, on_delete=models.PROTECT)
    tractor_plate = models.ForeignKey(Tractors, on_delete=models.PROTECT)
    trailer_plate = models.ForeignKey(Trailers, on_delete=models.PROTECT)
    tractor_fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES)
    backpack_fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES)
    chamber_fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES)
    tractor_liters = models.PositiveIntegerField()
    backpack_liters = models.PositiveIntegerField()
    chamber_liters = models.PositiveIntegerField()
    # -1 means not required (full)
    tractor_liters_to_load = models.IntegerField(default=-1)
    backpack_liters_to_load = models.IntegerField(default=-1)
    chamber_liters_to_load = models.IntegerField(default=-1)

    requires_odometer = models.BooleanField(default=False)
    requires_kilometers = models.BooleanField(default=False)
    is_blocked = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=True)
    in_agreement = models.IntegerField(choices=AGREEMENT_CHOICES, default=0)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.operation_code = secrets.token_hex(3)
            while FuelOrders.objects.filter(
                operation_code=self.operation_code
            ).exists():
                self.operation_code = secrets.token_hex(3)
        super().save(*args, **kwargs)

    def get_total_liters(self):
        return self.tractor_liters + self.backpack_liters + self.chamber_liters

    def __str__(self):
        return self.operation_code


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
