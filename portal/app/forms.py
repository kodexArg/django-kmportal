from django import forms
from .models import FuelOrders, Drivers, Tractors, Trailers


# Company Details Forms
class FuelOrderForm(forms.ModelForm):
    class Meta:
        model = FuelOrders
        exclude = ['operation_code']

    def clean_operation_code(self):
        return self.cleaned_data.get('operation_code') or 'default'


class CreateDriverForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = [
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
        ]


class UpdateDriverForm(forms.ModelForm):
    class Meta:
        model = Drivers
        fields = [
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
            "is_active",
            "is_deleted"
        ]


class DeleteDriverForm(forms.Form):
    id = forms.IntegerField()


class TractorForm(forms.ModelForm):
    class Meta:
        model = Tractors
        fields = ["domain"]

    
class TrailerForm(forms.ModelForm):
    class Meta:
        model = Trailers
        fields = ["domain"]

