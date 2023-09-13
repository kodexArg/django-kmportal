from app.models import FuelOrders
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
from portal.custom_storage import DocumentStorage
from datetime import datetime

def get_filename(instance, filename):
    today = datetime.now()
    year = today.year
    month = today.month
    day = today.day
    operation_code = instance.fuel_order.operation_code
    field_name = filename.split('.')[0]  # Assuming the filename comes in as 'field_name.extension'
    
    return f"{year}/{month}/{day}/{operation_code}_{field_name}.jpg"


class Refuelings(models.Model):
    """Core Table of the refueling Workflow: STEP 2"""

    acceptance_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    fuel_order = models.OneToOneField("app.FuelOrders", on_delete=models.CASCADE)
    pump_operator = models.ForeignKey(User, limit_choices_to={'groups__name': 'Pump Operators'}, on_delete=models.CASCADE)

    tractor_pic = models.ImageField(upload_to=get_filename, storage=DocumentStorage(), null=True, blank=True)
    backpack_pic = models.ImageField(upload_to=get_filename, storage=DocumentStorage(), null=True, blank=True)
    chamber_pic = models.ImageField(upload_to=get_filename, storage=DocumentStorage(), null=True, blank=True)

    tractor_liters = models.PositiveIntegerField(default=0)
    backpack_liters = models.PositiveIntegerField(default=0)
    chamber_liters = models.PositiveIntegerField(default=0)

    tractor_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)
    backpack_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)
    chamber_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)

    dispatch_note_pic = models.ImageField(upload_to=get_filename, storage=DocumentStorage(), null=True, blank=True)
    observation_pic = models.ImageField(upload_to=get_filename, storage=DocumentStorage(), null=True, blank=True)
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
