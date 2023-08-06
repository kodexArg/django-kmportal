from app.models import FuelOrders
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
from loguru import logger


class Refuelings(models.Model):
    """Core Table of the refueling Workflow: STEP 2"""

    acceptance_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    fuel_order = models.OneToOneField("app.FuelOrders", on_delete=models.CASCADE)
    pump_operator = models.ForeignKey(User, limit_choices_to={'groups__name': 'Pump Operators'}, on_delete=models.CASCADE)

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

    is_finished = models.BooleanField(default=False)

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
