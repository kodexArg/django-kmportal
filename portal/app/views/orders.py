from django.urls import reverse
from app.forms import FuelOrderForm
from app.models import FuelOrders
from staff.models import Refuelings
from app.views.helpers import CustomTemplateView
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import RedirectView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from loguru import logger


@method_decorator(login_required, name="dispatch")
class OrderView(CustomTemplateView):
    template_name = "modules/order.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        operation_code = self.kwargs.get("operation_code")
        context["operation_code"] = operation_code
        order = FuelOrders.objects.get(operation_code=operation_code)
        context["order"] = order

        try:
            refueling = order.refuelings
            documents = refueling.documents.all()
            context["refueling"] = refueling
            context["documents"] = documents
        except Refuelings.DoesNotExist:
            context["refueling"] = None
        return context


@method_decorator(login_required, name="dispatch")
class OrdersListView(CustomTemplateView):
    template_name = "modules/orders.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = context.get("company")
        if company is not None:
            context["fuel_orders"] = FuelOrders.objects.filter(company=company)
        return context


@method_decorator(login_required, name="dispatch")
class OrderPauseView(RedirectView):
    def post(self, request, order_id, *args, **kwargs):
        fuel_order = get_object_or_404(FuelOrders, id=order_id)
        fuel_order.is_paused = not fuel_order.is_paused
        fuel_order.save()
        return HttpResponseRedirect(reverse("orders"))


@method_decorator(login_required, name="dispatch")
class OrderAgreementView(RedirectView):
    def post(self, request, order_id, *args, **kwargs):
        fuel_order = get_object_or_404(FuelOrders, id=order_id)
        fuel_order.in_agreement = "agreed"
        fuel_order.save()
        return HttpResponseRedirect(reverse("orders"))


@method_decorator(login_required, name="dispatch")
class OrderDeleteView(RedirectView):
    def post(self, request, order_id, *args, **kwargs):
        fuel_order = get_object_or_404(FuelOrders, id=order_id)
        logger.info(f"Deleting order {fuel_order}")
        fuel_order.delete()
        return HttpResponseRedirect(reverse("orders"))


class OrderJsonView(View):
    """Return a JSon object with the data for a single order.
    Used along with OrderListView
    """

    def get(self, request, *args, **kwargs):
        order_id = kwargs.get("order_id")
        fuel_order = get_object_or_404(FuelOrders, id=order_id)
        data = {
            "operation_code": fuel_order.operation_code,
            "user_creator": str(fuel_order.user_creator),
            "is_locked": fuel_order.is_locked,
            "is_paused": fuel_order.is_paused,
            "is_finished": fuel_order.is_finished,
            "order_date": fuel_order.order_date.isoformat(),
            "modified_date": fuel_order.modified_date.isoformat(),
            "driver": str(fuel_order.driver),
            "tractor_plate": str(fuel_order.tractor_plate),
            "trailer_plate": str(fuel_order.trailer_plate),
            "formated_tractor_liters_to_load_of": fuel_order.formated_tractor_liters_to_load_of,
            "formated_backpack_liters_to_load_of": fuel_order.formated_backpack_liters_to_load_of,
            "formated_chamber_liters_to_load_of": fuel_order.formated_chamber_liters_to_load_of,
            "tractor_liters": fuel_order.tractor_liters,
            "backpack_liters": fuel_order.backpack_liters,
            "chamber_liters": fuel_order.chamber_liters,
        }
        return JsonResponse(data)


class OrderBaseView(CustomTemplateView, FormView):
    template_name = "modules/create_order.html"
    success_url = "/orders/"

    def form_valid(self, form):
        fuel_order = form.save(commit=False)
        fuel_order.company = self.get_company(self.request.user, self.provider_name)
        fuel_order.user_lastmod = self.request.user
        fuel_order.save()
        return super().form_valid(form)

    # company is required by teh form to filter records
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        company = self.get_company(self.request.user, self.provider_name)
        kwargs.update({"company": company})
        return kwargs

    def form_invalid(self, form):
        logger.error(f"Error saving order: {form.errors}")
        return super().form_invalid(form)


@method_decorator(login_required, name="dispatch")
class OrderCreateView(OrderBaseView):
    form_class = FuelOrderForm

    def form_valid(self, form):
        form.instance.user_creator = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class OrderUpdateView(OrderBaseView):
    form_class = FuelOrderForm

    def get_object(self):
        order_id = self.kwargs.get("order_id")
        return get_object_or_404(FuelOrders, id=order_id)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"instance": self.get_object()})
        return kwargs
