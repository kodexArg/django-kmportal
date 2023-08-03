from django.contrib import admin
from regex import P

from staff.models import Refuelings, PumpOperator

# Register your models here.

admin.site.register(Refuelings)
admin.site.register(PumpOperator)
