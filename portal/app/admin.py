from django.contrib import admin
from .models import Company, CompanySocialAccount

# Register your models here.


admin.site.register(Company)
admin.site.register(CompanySocialAccount)
