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


class QrForm(forms.Form):
    operation_code = forms.CharField(max_length=6, widget=forms.TextInput(attrs={"class": "text-xl font-bold w-40 rounded-full text-center", "placeholder": "QR"}))

    def clean_operation_code(self):
        operation_code = self.cleaned_data.get("operation_code")
        try:
            FuelOrders.objects.get(operation_code=operation_code)
        except FuelOrders.DoesNotExist:
            raise forms.ValidationError("Invalid operation code")
        return operation_code



class RefuelingForm(forms.ModelForm):
    class Meta:
        model = Refuelings
        exclude = ['fuel_order', 'pump_operator', 'is_finished']

    def __init__(self, *args, **kwargs):
        self.fuel_order = kwargs.pop('fuel_order', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        if not self.fuel_order.is_locked or self.fuel_order.is_finished:
            raise forms.ValidationError("This operation code is not locked or finished")
        return super().clean()

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.fuel_order = self.fuel_order
        if commit:
            instance.save()
        return instance


