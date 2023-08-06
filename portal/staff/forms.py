from app.models import FuelOrders
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from staff.models import Refuelings


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Usuario"}),
        max_length=30,
        required=True,
        error_messages={"required": "Ingrese un usuario"},
        help_text="Usuario",
        )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Contraseña"}),
        max_length=30,
        required=True,
        error_messages={"required": "Ingrese una contraseña"},
        help_text="Contraseña",
        )
    



class RefuelingForm(forms.ModelForm):
    operation_code = forms.CharField(max_length=6)

    class Meta:
        model = Refuelings
        exclude = ['fuel_order', 'pump_operator', 'status']

    def clean_operation_code(self):
        operation_code = self.cleaned_data.get('operation_code')
        try:
            fuel_order = FuelOrders.objects.get(operation_code=operation_code)
        except FuelOrders.DoesNotExist:
            raise forms.ValidationError("Invalid operation code")
        if fuel_order.is_blocked or fuel_order.is_finished:
            raise forms.ValidationError("This operation code is already in use or finished")
        return operation_code

    def save(self, commit=True):
        instance = super().save(commit=False)
        operation_code = self.cleaned_data.get('operation_code')
        fuel_order = FuelOrders.objects.get(operation_code=operation_code)
        fuel_order.is_blocked = True
        fuel_order.save()
        instance.fuel_order = fuel_order
        if commit:
            instance.save()
        return instance
   

class QrForm(forms.Form):
    operation_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'class': 'text-xl font-bold w-40 rounded-full text-center', 'placeholder': 'QR'}))

    def clean_operation_code(self):
        operation_code = self.cleaned_data.get('operation_code')
        try:
            FuelOrders.objects.get(operation_code=operation_code)
        except FuelOrders.DoesNotExist:
            raise forms.ValidationError("Invalid operation code")
        return operation_code
