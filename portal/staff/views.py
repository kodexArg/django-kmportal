import json
from app.models import FuelOrders, ExtraCash
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Prefetch
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import FormView
from loguru import logger
from staff.forms import DocumentForm  # Import the DocumentForm
from staff.forms import CustomLoginForm, QrForm, RefuelingForm  # Import your forms
from staff.models import Documents, FuelOrders, Refuelings  # Import your models
from icecream import ic
# Create a formset for the Documents model
DocumentFormSet = inlineformset_factory(Refuelings, Documents, form=DocumentForm, extra=1, can_delete=False)


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

# Create a formset for the Documents model
DocumentFormSet = inlineformset_factory(Refuelings, Documents, form=DocumentForm, extra=1, can_delete=False)


class StaffExtracashView(ListView):
    template_name = "staff/extracash.html"
    model = ExtraCash


from django.core.files.storage import FileSystemStorage

class StaffExtracashAttend(View):
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request, operation_code):
        print(request.FILES)
        try:
            order = ExtraCash.objects.get(operation_code=operation_code)

            # Handle file upload
            if 'document' in request.FILES:
                myfile = request.FILES['document']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)

                # Assuming your model has a field called 'document'
                order.document = filename  # You save the reference to the uploaded file to the model

            order.is_finished = True
            order.save()

            return JsonResponse({"status": "success", "message": "Order status updated successfully."})
        except ExtraCash.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Order not found."}, status=404)


# TODO: authorized user only
class StaffRefuelingView(FormView):
    template_name = "staff/new.html"
    form_class = RefuelingForm

    def post(self, request, *args, **kwargs):
        logger.info("Post method called")
        return super().post(request, *args, **kwargs)

    # Fetch the FuelOrders instance based on the operation_code
    def get_fuel_order(self):
        operation_code = self.kwargs.get("operation_code")
        return get_object_or_404(FuelOrders, operation_code=operation_code)

    def get(self, request, *args, **kwargs):
        self.fuel_order = self.get_fuel_order()
        return super().get(request, *args, **kwargs)

    # Inject the fuel_order instance into the form kwargs
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        self.fuel_order = self.get_fuel_order()
        if self.fuel_order:
            self.fuel_order.is_locked = True
            self.fuel_order.save()
            kwargs["fuel_order"] = self.fuel_order
            logger.info(f"Fuel order found and locked. ID: {self.fuel_order.id}")
            return kwargs
        else:
            logger.error(f"Fuel order not found")
            return redirect("staff_home")

    # Add the DocumentFormSet to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        temp_refueling = Refuelings()  # Create a temporary instance
        context["fuel_order"] = self.get_fuel_order()

        if self.request.POST:
            context["document_formset"] = DocumentFormSet(self.request.POST, self.request.FILES, instance=temp_refueling)
        else:
            context["document_formset"] = DocumentFormSet(instance=temp_refueling)
        return context

    # Handle form submission
    def form_valid(self, form):
        logger.info(f"Form is valid. Refueling data: {form.cleaned_data}")

        # Create or update the Refuelings instance
        refueling = form.save(commit=False)
        refueling.pump_operator = self.request.user
        refueling.is_finished = True
        refueling.save()
        logger.info(f"Refueling saved successfully. ID: {refueling.id}")

        # Update the FuelOrders instance
        for field in ["tractor_liters", "backpack_liters", "chamber_liters"]:
            field_value = form.cleaned_data.get(field)
            if field_value:
                setattr(self.fuel_order, field, field_value)
        self.fuel_order.is_finished = True
        self.fuel_order.save()
        logger.info(f"Fuel order saved successfully. ID: {self.fuel_order.id}")

        # Handle the uploaded files and their descriptions
        document_formset = DocumentFormSet(self.request.POST, self.request.FILES, instance=refueling)
        if document_formset.is_valid():
            instances = document_formset.save(commit=False)
            for instance in instances:
                print(self.request.FILES)
                instance.refueling = refueling
                instance.save()


        return redirect("staff_home")

    # Handle form errors
    def form_invalid(self, form):
        logger.error(f"Form is invalid. Errors: {form.errors}")
        return super().form_invalid(form)

    # URL to redirect to upon successful form submission
    def get_success_url(self):
        return reverse("staff_orders")





class StaffQrView(FormView):
    template_name = "staff/qr.html"
    form_class = QrForm

    def form_valid(self, form):
        operation_code = form.cleaned_data.get("operation_code")
        fuel_order = FuelOrders.objects.get(operation_code=operation_code)
        if fuel_order.is_finished:
            form.add_error(None, "Esta orden ya fue finalizada y no se puede modificar por este medio.")
            return self.form_invalid(form)

        return redirect("staff_refueling", operation_code=operation_code, was_locked=fuel_order.is_locked)


## Helper
def handle_qr_code(request):
    body = json.loads(request.body)
    decoded_text = body.get("decoded_text")
    logger.info(f"decoded text: {decoded_text}")

    return JsonResponse({"status": "success"})


class StaffListOrdersView(ListView):
    template_name = "staff/orders.html"
    context_object_name = "orders"

    def get_queryset(self):
        refuelings = Refuelings.objects.all()
        queryset = FuelOrders.objects.prefetch_related(Prefetch("refuelings", queryset=refuelings))

        return queryset
