from app.models import FuelOrders
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
from portal.custom_storage import DocumentStorage
from datetime import datetime
from loguru import logger
import random
import string


def get_filename(instance, filename):
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    time = today.strftime("%H%M%S")
    operation_code = instance.fuel_order.operation_code
    logger.info(f">>> Operation Code: {operation_code}")

    # Generate a random string of length 8
    random_string = "".join(random.choices(string.ascii_letters + string.digits, k=5))
    logger.info(f">>> {random_string}")

    return f"extracash/{year}/{month}/{day}/{operation_code}/{random_string}_{time}.jpg"


class RefuelingsManager(models.Manager):
    def sorted_by_edited_date(self):
        return self.get_queryset().order_by('edited_date')

    def sorted_by_acceptance_date(self):
        return self.get_queryset().order_by('acceptance_date')


class Refuelings(models.Model):
    """Core Table of the refueling Workflow: STEP 2"""
    objects = RefuelingsManager()

    acceptance_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    fuel_order = models.OneToOneField("app.FuelOrders", on_delete=models.CASCADE)
    pump_operator = models.ForeignKey(User, limit_choices_to={"groups__name": "Pump Operators"}, on_delete=models.CASCADE)

    tractor_liters = models.PositiveIntegerField(default=0) 
    backpack_liters = models.PositiveIntegerField(default=0) 
    chamber_liters = models.PositiveIntegerField(default=0) 

    tractor_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)
    backpack_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)
    chamber_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)

    observation = models.CharField(max_length=512, null=True, blank=True)

    is_finished = models.BooleanField(default=False)

    def clean(self):
        if self.pk:
            old_instance = Refuelings.objects.get(pk=self.pk)
            if old_instance.is_finished and not self.is_finished:
                raise ValidationError("You cannot modify this refueling as it has already been finished. Please contact the administrator for further assistance.")
        super().clean()

    def __str__(self):
        return str(self.fuel_order.operation_code)

    def get_total_liters(self):
        return self.tractor_liters + self.backpack_liters + self.chamber_liters


class Documents(models.Model):
    refueling = models.ForeignKey(Refuelings, related_name="documents", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    filename = models.ImageField(upload_to=get_filename, storage=DocumentStorage())
