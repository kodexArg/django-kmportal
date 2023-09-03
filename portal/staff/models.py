from app.models import FuelOrders
from django.db import models
from django.forms import ValidationError
from django.contrib.auth.models import User
from loguru import logger
from portal.custom_storage import DocumentStorage
import os
import datetime



def rename_upload_file(instance, filename):
    # Get the file extension
    ext = filename.split('.')[-1]

    # Get the current date to construct folder paths
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day

    # Create the directory path
    dir_path = os.path.join('static/documents', str(year), str(month).zfill(2), str(day).zfill(2))

    # Check if the directory exists, if not, create it
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # Create the new filename using the operation code
    new_filename = f"{instance.fuel_order.operation_code}-{filename}"

    # Return the complete path
    return os.path.join(dir_path, new_filename)


class Refuelings(models.Model):
    """Core Table of the refueling Workflow: STEP 2"""

    acceptance_date = models.DateField(auto_now_add=True)
    edited_date = models.DateField(auto_now=True)
    fuel_order = models.OneToOneField("app.FuelOrders", on_delete=models.CASCADE)
    pump_operator = models.ForeignKey(User, limit_choices_to={'groups__name': 'Pump Operators'}, on_delete=models.CASCADE)

    tractor_pic = models.ImageField(upload_to=rename_upload_file, storage=DocumentStorage(), null=True, blank=True)
    backpack_pic = models.ImageField(upload_to=rename_upload_file, storage=DocumentStorage(), null=True, blank=True)
    chamber_pic = models.ImageField(upload_to=rename_upload_file, storage=DocumentStorage(), null=True, blank=True)

    tractor_liters = models.PositiveIntegerField(default=0)
    backpack_liters = models.PositiveIntegerField(default=0)
    chamber_liters = models.PositiveIntegerField(default=0)

    tractor_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)
    backpack_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)
    chamber_fuel_type = models.CharField(max_length=50, choices=FuelOrders.FUEL_TYPE_CHOICES, null=True, blank=True)

    dispatch_note_pic = models.ImageField(upload_to="operation_code/dispatch_note", null=True, blank=True)
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
