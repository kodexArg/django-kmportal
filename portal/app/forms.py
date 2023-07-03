from django import forms
from .models import FuelOrders, Drivers, Tractors, Trailers


class FuelOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company'].required = False
        self.fields['expiration_date'].required = False
        self.fields['in_agreement'].required = False

    def clean_company(self):
        company = self.cleaned_data.get('company')
        if not company:
            raise forms.ValidationError("Company is required.")
        return company

    def clean(self):
        cleaned_data = super().clean()
        expiration_date = cleaned_data.get('expiration_date')
        in_agreement = cleaned_data.get('in_agreement')

        # Handle the validation for 'expiration_date' and 'in_agreement'
        # based on your requirements
        if not expiration_date:
            raise forms.ValidationError("Expiration date is required.")
        if not in_agreement:
            raise forms.ValidationError("In agreement field is required.")

        return cleaned_data
    
    class Meta:
        model = FuelOrders
        exclude = ["operation_code"]



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
            "is_deleted",
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

