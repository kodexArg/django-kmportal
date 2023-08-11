from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
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
                        messages.error(request, "No estás registrado como operador de bomba")
                else:
                    messages.error(request, "No tienes permiso para ingresar en este sitio")
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
        fuel_order = FuelOrders.objects.get(operation_code=operation_code)
        if fuel_order.is_finished:
            form.add_error(None, "This fuel order has already been completed. Please enter a new order.")
            return self.form_invalid(form)
        return redirect("staff_refueling", operation_code=operation_code, was_locked=fuel_order.is_locked)


class StaffRefuelingView(FormView):
    template_name = "staff/refueling.html"
    form_class = RefuelingForm

    def get_fuel_order(self):
        operation_code = self.kwargs.get("operation_code")
        return get_object_or_404(FuelOrders, operation_code=operation_code)

    def get(self, request, *args, **kwargs):
        """ ... [rest of your get method] ... """
        self.fuel_order = self.get_fuel_order()
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        """Sending fuel_order record to the form based on the operation_code received from qr"""
        kwargs = super().get_form_kwargs()
        self.fuel_order = self.get_fuel_order()
        # if the fuel order exists, lock it
        if self.fuel_order:
            self.fuel_order.is_locked = True
            self.fuel_order.save()
            kwargs["fuel_order"] = self.fuel_order
            return kwargs
        else:
            # this should be handled by the qr view. Just in case the user change the GET url...
            logger.error(f"Fuel order not found")
            return redirect("staff_home")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.fuel_order = self.get_fuel_order()
        context['fuel_order'] = self.fuel_order
        return context
    
    def form_valid(self, form):
        refueling = form.save(commit=False)
        refueling.pump_operator = self.request.user
        refueling.is_finished = True
        refueling.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("staff_home")