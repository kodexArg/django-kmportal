from loguru import logger
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.views import View
from staff.forms import CustomLoginForm
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import TemplateView


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
                    login(request, user)
                    messages.success(request, "Ingreso correcto")
                    return redirect("staff_home")
                else:
                    messages.error(request, "Tu usuario es correcto pero no tienes permiso para ingresar en este sitio")
            else:
                messages.error(request, "Usuario o contraseña incorrectos")
        else:
            messages.error(request, "Los datos ingresados son incorrectos")

        # Redirect to GET request if form is invalid or login fails
        return redirect("staff_home")

### AUTHORIZED PAGES ###

#similar to orders.py it shows the orders that are pending from all companies
@method_decorator(staff_member_required, name="dispatch")
class StaffRefillView(TemplateView):
    template_name = "staff/refill.html"


    