from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.exceptions import PermissionDenied
from django.forms import ValidationError
from app.models import FuelOrders


class PumpOperatorManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        raise PermissionDenied("PumpOperator cannot be a superuser")


class PumpOperator(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = PumpOperatorManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username


# Create your models here.
class Refuelings(models.Model):
    """Core Table of the refueling Workflow: STEP 2"""

    ACCEPTANCE_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("attending", "Attending"),
        ("finished", "Finished"),
        ("locked", "Locked"),
    ]

    acceptance_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    fuel_order = models.ForeignKey("app.FuelOrders", on_delete=models.CASCADE)
    pump_operator = models.ForeignKey(PumpOperator, on_delete=models.CASCADE)
    status = models.CharField(choices=ACCEPTANCE_STATUS_CHOICES, default="pending", max_length=10)

    tractor_pic = models.ImageField(upload_to="operation_code/tractor")
    backpack_pic = models.ImageField(upload_to="operation_code/backpack")
    chamber_pic = models.ImageField(upload_to="operation_code/chamber")

    tractor_liters = models.PositiveIntegerField(default=0)
    backpack_liters = models.PositiveIntegerField(default=0)
    chamber_liters = models.PositiveIntegerField(default=0)

    tractor_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES)
    backpack_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES)
    chamber_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES)

    dispatch_note_pic = models.ImageField(upload_to="operation_code/dispatch_note")
    observation_pic = models.ImageField(upload_to="operation_code/others", null=True, blank=True)
    observation = models.CharField(max_length=512, null=True, blank=True)

    def clean(self):
        if self.pk:  # check if this instance is already saved in the database
            old_instance = Refuelings.objects.get(pk=self.pk)  # retrieve the old instance
            if old_instance.status == "finished" and self.status != "finished":
                raise ValidationError("You cannot modify this refueling as it has already been finished. Please contact the administrator for further assistance.")
        super().clean()

    def __str__(self):
        return str(self.fuel_order.operation_code)

    def get_total_liters(self):
        return self.tractor_liters + self.backpack_liters + self.chamber_liters

