from django.contrib import admin
from .models import (
    Company, 
    CompanySocialAccount,
    Drivers
    )

# Register your models here.


admin.site.register(Company)
admin.site.register(CompanySocialAccount)
admin.site.register(Drivers)