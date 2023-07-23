from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from pytz import timezone
from app.views.helpers import CustomTemplateView

from app.forms import ExtraCashForm
from app.models import ExtraCash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView
from django.utils import timezone

from loguru import logger


@method_decorator(login_required, name="dispatch")
class ExtraCashView(CustomTemplateView):
    template_name = "modules/extracash.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = context.get("company")
        context['form'] = ExtraCashForm()  # Add this line
        if company is not None:
            context["extracash"] = ExtraCash.objects.filter(company=company)
            context["extracash_orders"] = ExtraCash.objects.filter(company=company)

        return context

    def post(self, request, *args, **kwargs):
        logger.info(f'POST request received: \n{ request.POST }')
        if 'delete' in request.POST:
            # It's a delete operation
            id_to_delete = request.POST['delete']
            extracash_order = ExtraCash.objects.get(id=id_to_delete)
            extracash_order.delete()
            return redirect("extracash")
        else:
            # It's a form submission
            form = ExtraCashForm(request.POST)
            if form.is_valid():
                extracash_order = form.save(commit=False)
                extracash_order.company = self.get_company(request.user, self.provider_name)

                extracash_order.save()

                # Cookie:
                response = redirect("extracash")
                current_time = timezone.now()
                response.set_cookie('last_order_id', extracash_order.id)
                response.set_cookie('last_order_timestamp', current_time.isoformat())
                
                return response

            logger.error(form.errors)
            logger.error("Form is not valid")

            context = self.get_context_data(**kwargs)
            context["form"] = form
            return redirect("extracash")



