from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from app.views.helpers import CustomTemplateView

from app.forms import ExtraCashForm
from app.models import ExtraCash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from loguru import logger


@method_decorator(login_required, name="dispatch")
class ExtraCashListView(CustomTemplateView):
    template_name = "modules/extracash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = context.get("company")
        context['form'] = ExtraCashForm()  # Add this line
        if company is not None:
            context["extracash"] = ExtraCash.objects.filter(company=company)
        return context

    def post(self, request, *args, **kwargs):
        form = ExtraCashForm(request.POST)
        if form.is_valid():
            extracash_order = form.save(commit=False)
            extracash_order.company = self.get_company(request.user, self.provider_name)
            extracash_order.save()
            return redirect("extracash")

        logger.error(form.errors)
        logger.error("Form is not valid")

        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class ExtraCashViewCancel(RedirectView):
    pattern_name = "extracash"

    def post(self, request, order_id, *args, **kwargs):
        extracash_order = get_object_or_404(ExtraCash, id=order_id)
        action = request.POST.get("action")
        if action == "cancel":
            logger.info("Cancelling order")
            extracash_order.is_canceled = not extracash_order.is_canceled
            extracash_order.save()
        elif action == "delete":
            logger.info("Deleting order")
            extracash_order.delete()
            logger.info("Order deleted")

        return JsonResponse({"result": "success"})


class ExtraCashDataView(View):
    def get(self, request, *args, **kwargs):
        order_id = kwargs.get("order_id")
        extracash_order = get_object_or_404(ExtraCash, id=order_id)
        data = {
            "operation_code": extracash_order.operation_code,
            "order_date": extracash_order.order_date.isoformat(),
            "modified_date": extracash_order.modified_date.isoformat(),
            "requested_date": extracash_order.requested_date.isoformat(),
            "expiration_date": extracash_order.expiration_date.isoformat(),
            "user_creator": str(extracash_order.user_creator),
            "user_lastmod": str(extracash_order.user_lastmod),
            "company": str(extracash_order.company),
            "driver": str(extracash_order.driver),
            "is_blocked": extracash_order.is_blocked,
            "is_canceled": extracash_order.is_canceled,
            "is_finished": extracash_order.is_finished,
            "cancel_reason": extracash_order.cancel_reason,
            "in_agreement": extracash_order.in_agreement,
            "comments": extracash_order.comments,
            "cash_amount": extracash_order.cash_amount,
        }
        return JsonResponse(data)
