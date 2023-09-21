from app.models import FuelOrders
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from staff.models import Refuelings
from django import forms
from staff.models import Documents
from django.forms import formset_factory
from django import forms
from django.forms import FileInput


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Documents
        fields = ["filename"]
        widgets = {
            "filename": FileInput(
                attrs={
                    "class": "font-rubik leading-none text-xs bg-gray-50 rounded-md m-0 px-2 py-0 cursor-pointer text-center border border-gray-500",
                }
            ),
        }


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
    observation = forms.CharField(required=False)

    class Meta:
        model = Refuelings
        exclude = ["fuel_order", "pump_operator", "is_finished"]

    def __init__(self, *args, **kwargs):
        self.fuel_order = kwargs.pop("fuel_order", None)
        super().__init__(*args, **kwargs)
        if self.fuel_order and self.fuel_order.tractor_liters_to_load == 0:
            self.fields["tractor_liters"].initial = 0
            self.fields["tractor_liters"].disabled = True

        if self.fuel_order and self.fuel_order.chamber_liters_to_load == 0:
            self.fields["chamber_liters"].initial = 0
            self.fields["chamber_liters"].disabled = True

        if self.fuel_order and self.fuel_order.backpack_liters_to_load == 0:
            self.fields["backpack_liters"].initial = 0
            self.fields["backpack_liters"].disabled = True

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
