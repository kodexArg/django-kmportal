from app.forms import FuelOrderForm
from app.models import FuelOrders
from app.views.helpers import CustomTemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import RedirectView
from loguru import logger


@method_decorator(login_required, name="dispatch")
class FuelOrderListView(CustomTemplateView):
    template_name = "modules/orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = context.get("company")
        if company is not None:
            context["fuel_orders"] = FuelOrders.objects.filter(company=company)
        return context

    def post(self, request, *args, **kwargs):
        form = FuelOrderForm(request.POST)
        if form.is_valid():
            fuel_order = form.save(commit=False)
            fuel_order.company = self.get_company(request.user, self.provider_name)

            # Check if all liters values are zero
            if all(
                tank == -1
                for tank in [
                    fuel_order.tractor_liters,
                    fuel_order.backpack_liters,
                    fuel_order.chamber_liters,
                ]
            ):
                form.add_error(None, "All liters values cannot be zero.")
                logger.error("All liters values are zero.")
                context = self.get_context_data(**kwargs)
                context["form"] = form
                return render(request, self.template_name, context)

            # Check if a non-zero liters value has a fuel_type field with a value different from empty
            if fuel_order.tractor_liters != None and not fuel_order.tractor_fuel_type:
                form.add_error(
                    "tractor_fuel_type",
                    "Fuel type is required for non-zero liters value.",
                )
                logger.error("Fuel type is missing for non-zero tractor liters value.")
                context = self.get_context_data(**kwargs)
                context["form"] = form
                return render(request, self.template_name, context)

            # Repeat the same checks for backpack_liters and chamber_liters if needed
            if fuel_order.backpack_liters != None and not fuel_order.backpack_fuel_type:
                form.add_error(
                    "backpack_fuel_type",
                    "Fuel type is required for non-zero liters value.",
                )
                logger.error("Fuel type is missing for non-zero backpack liters value.")
                context = self.get_context_data(**kwargs)
                context["form"] = form
                return render(request, self.template_name, context)

            if fuel_order.chamber_liters != None and not fuel_order.chamber_fuel_type:
                form.add_error(
                    "chamber_fuel_type",
                    "Fuel type is required for non-zero liters value.",
                )
                logger.error("Fuel type is missing for non-zero chamber liters value.")
                context = self.get_context_data(**kwargs)
                context["form"] = form
                return render(request, self.template_name, context)

            # Check if the order is canceled
            if fuel_order.is_canceled:
                form.add_error(None, "Order cannot be canceled.")
                logger.error("Order cannot be canceled.")
                context = self.get_context_data(**kwargs)
                context["form"] = form
                return render(request, self.template_name, context)

            fuel_order.save()
            return redirect("orders")

        logger.error(form.errors)
        logger.error("Form is not valid")

        # If the form is invalid, re-render the template with the form and display the errors
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class FuelOrderViewNewOrEdit(CustomTemplateView):
    """Add new or edit order by order_id. Used along with FuelOrderListView"""

    template_name = "modules/single_order.html"

    def get_context_data(self, order_id=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if order_id:
            fuel_order = get_object_or_404(FuelOrders, id=order_id)
            form = FuelOrderForm(instance=fuel_order)
        else:
            form = FuelOrderForm()

        context["form"] = form
        return context


@method_decorator(login_required, name="dispatch")
class FuelOrderViewCancel(RedirectView):
    pattern_name = "orders"  # redirect to this after cancel or delete

    def post(self, request, order_id, *args, **kwargs):
        # Get the FuelOrders record with the given order_id
        fuel_order = get_object_or_404(FuelOrders, id=order_id)

        # Check the action type
        action = request.POST.get("action")
        if action == "cancel":
            logger.info("Cancelling order")
            fuel_order.is_canceled = not fuel_order.is_canceled
            fuel_order.save()
        elif action == "delete":
            logger.info("Deleting order")
            fuel_order.delete()  # Permanently delete the order
            logger.info("Order deleted")

        return JsonResponse({"result": "success"})


class FuelOrderDataView(View):
    """Return a JSon object with the data for a single order.
    Used along with FuelOrderListView
    """

    def get(self, request, *args, **kwargs):
        order_id = kwargs.get("order_id")
        fuel_order = get_object_or_404(FuelOrders, id=order_id)
        data = {
            "operation_code": fuel_order.operation_code,
            "user_creator": str(fuel_order.user_creator),
            "is_blocked": fuel_order.is_blocked,
            "is_canceled": fuel_order.is_canceled,
            "is_finished": fuel_order.is_finished,
            "order_date": fuel_order.order_date.isoformat(),
            "modified_date": fuel_order.modified_date.isoformat(),
            "driver": str(fuel_order.driver),
            "tractor_plate": str(fuel_order.tractor_plate),
            "trailer_plate": str(fuel_order.trailer_plate),
            "formated_tractor_liters_to_load_of": fuel_order.tractor_liters_to_load,
            "formated_backpack_liters_to_load_of": fuel_order.backpack_liters_to_load,
            "formated_chamber_liters_to_load_of": fuel_order.chamber_liters_to_load,
        }
        return JsonResponse(data)