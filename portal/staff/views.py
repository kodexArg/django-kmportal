from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from loguru import logger
from app.models import FuelOrders
from staff.forms import CustomLoginForm, QrForm, RefuelingForm

### UNAUTHORIZED PAGES ###


class StaffHomeView(View):
    template_name = "staff/home.html"

    def get(self, request):
        form = CustomLoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff:
                    # Check if the user is in the "Pump Operators" group
                    if Group.objects.get(name="Pump Operators") in user.groups.all():
                        login(request, user)
                        messages.success(request, "Ingreso correcto")
                        return redirect("staff_home")
                    else:
                        messages.error(request, "Tu usuario es correcto pero no eres un operador de bomba")
                else:
                    messages.error(request, "Tu usuario es correcto pero no tienes permiso para ingresar en este sitio")
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Los datos ingresados son incorrectos")

        # Redirect to GET request if form is invalid or login fails
        return redirect("staff_home")


### AUTHORIZED PAGES ###


class StaffQrView(FormView):
    template_name = "staff/qr.html"
    form_class = QrForm

    def form_valid(self, form):
        operation_code = form.cleaned_data.get("operation_code")
        return redirect("staff_refueling", operation_code=operation_code)


class StaffRefuelingView(FormView):
    template_name = "staff/refueling.html"
    form_class = RefuelingForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        operation_code = self.kwargs.get("operation_code")
        self.fuel_order = get_object_or_404(FuelOrders, operation_code=operation_code)
        return kwargs

    def form_valid(self, form):
        refueling = form.save(commit=False)
        refueling.pump_operator = self.request.user
        refueling.status = "pending"
        refueling.save()
        return super().form_valid(form)

    def get_success_url(self):
        return redirect("staff_home")
