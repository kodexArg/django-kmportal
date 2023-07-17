from app.forms import (CreateDriverForm, DeleteDriverForm, TractorForm,
                       TrailerForm, UpdateDriverForm)
from app.models import CompanySocialAccount, Drivers, Tractors, Trailers
from app.views.helpers import CustomTemplateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from loguru import logger


# Company #
@method_decorator(login_required, name="dispatch")
class CompanyView(CustomTemplateView):
    template_name = "modules/company.html"

    def dispatch(self, request, *args, **kwargs):
        """overriding dispatch method"""
        if self.request.user.is_authenticated:
            try:
                social_account = self.request.user.socialaccount_set.get(provider=self.provider_name)
                company_social_account = CompanySocialAccount.objects.get(social_account=social_account)
                if company_social_account.company is None:
                    return redirect("user_home")
            except CompanySocialAccount.DoesNotExist:
                return redirect("user_home")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Multi Forms handler
        update form for each field then create a form to add new fields
        'from_type' is a hidden field to swtich from update to create form
        """

        # Create form
        form_type = request.POST.get("form_type")
        if form_type == "create_driver":
            form = CreateDriverForm(request.POST)
            if form.is_valid():
                driver = form.save(commit=False)
                driver.company = self.get_company(request.user, self.provider_name)
                driver.save()
                return redirect("company")
            else:
                logger.error(form.errors)

        # Update form
        elif form_type == "update_driver":
            driver_id = request.POST.get("driver_id")
            driver = Drivers.objects.get(id=driver_id)
            form = UpdateDriverForm(request.POST, instance=driver)
            if form.is_valid():
                form.save()
                return redirect("company")
            else:
                logger.error(form.errors)

        # Delete form
        elif form_type == "delete_driver":
            driver_id = request.POST.get("driver_id")
            driver = Drivers.objects.get(id=driver_id)
            driver.delete()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = context.get("company")
        if company is not None:
            context["drivers"] = Drivers.objects.filter(company=company)
        context["create_form"] = CreateDriverForm(prefix="create")
        context["update_form"] = UpdateDriverForm(prefix="update")
        context["delete_form"] = DeleteDriverForm(prefix="delete")
        return context


# Vehicles #
@method_decorator(login_required, name="dispatch")
class VehiclesView(CustomTemplateView):
    template_name = "modules/vehicles.html"

    def post(self, request, *args, **kwargs):
        # Create and update form for tractors

        form_type = request.POST.get("form_type")
        if form_type == "create_tractor":
            form = TractorForm(request.POST)
            if form.is_valid():
                tractor = form.save(commit=False)
                tractor.company = self.get_company(request.user, self.provider_name)
                tractor.domain  # ?
                tractor.save()
                return redirect("vehicles")
            else:
                logger.error(form.errors)

        elif form_type == "update_tractor":
            tractor_id = request.POST.get("tractor_id")
            tractor = Tractors.objects.get(id=tractor_id)
            form = TractorForm(request.POST, instance=tractor)
            if form.is_valid():
                form.save()
                return redirect("vehicles")
            else:
                logger.error(form.errors)

        # Create and update form for trailers
        elif form_type == "create_trailer":
            form = TrailerForm(request.POST)
            if form.is_valid():
                trailer = form.save(commit=False)
                trailer.company = self.get_company(request.user, self.provider_name)
                trailer.save()
                return redirect("vehicles")
            else:
                logger.error(form.errors)

        elif form_type == "update_trailer":
            trailer_id = request.POST.get("trailer_id")
            trailer = Trailers.objects.get(id=trailer_id)
            form = TrailerForm(request.POST, instance=trailer)
            if form.is_valid():
                form.save()
                return redirect("vehicles")
            else:
                logger.error(form.errors)

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        company = context.get("company")
        if company is not None:
            context["tractors"] = Tractors.objects.filter(company=company)
            context["trailers"] = Trailers.objects.filter(company=company)
        context["create_tractor_form"] = TractorForm(prefix="create")
        context["update_tractor_form"] = TractorForm(prefix="update")
        context["create_trailer_form"] = TrailerForm(prefix="create")
        context["update_trailer_form"] = TrailerForm(prefix="update")
        return context
