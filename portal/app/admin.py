from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import (
    CompanySocialAccount,
    FuelOrders,
    Trailers,
    Company, 
    Drivers,
    Tractors,
    Setting,
    )


# Register your models here.
admin.site.register(CompanySocialAccount)
admin.site.register(FuelOrders)
admin.site.register(Trailers)
admin.site.register(Tractors)
admin.site.register(Setting)
admin.site.register(Company)
admin.site.register(Drivers)