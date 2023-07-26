from dataclasses import field
from django import forms
from django.contrib.auth.forms import AuthenticationForm


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
    
    
