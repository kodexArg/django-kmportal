from loguru import logger
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import TemplateView
from app.forms import (
    CreateDriverForm,
    UpdateDriverForm,
    DeleteDriverForm,
    TractorForm,
    TrailerForm,
)

from app.models import CompanySocialAccount, Drivers, Tractors, Trailers


class CustomTemplateView(TemplateView):
    """Used instead of TemplateView to add a custom context_data method"""

    provider_name = "Google"

    # context["provider_id"]
    def get_provider_id(self, user, provider_name):
        try:
            social_account = user.socialaccount_set.get(provider=provider_name)
            return social_account.get_provider().id
        except user.socialaccount_set.model.DoesNotExist:
            return None

    # context["company"]
    def get_company(self, user, provider_name):
        try:
            social_account = user.socialaccount_set.get(provider=provider_name)
            return social_account.companysocialaccount.company
        except (
            user.socialaccount_set.model.DoesNotExist,
            CompanySocialAccount.DoesNotExist,
        ):
            print("Company does not exist")
            return None

    # Context data getter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["provider_id"] = self.get_provider_id(
                self.request.user, self.provider_name
            )
            context["company"] = self.get_company(self.request.user, self.provider_name)
        return context


### UNAUTHORIZED PAGES ###
class HomeView(CustomTemplateView):
    template_name = "home.html"


class AboutUsView(CustomTemplateView):
    template_name = "about_us.html"


class ContactUsView(CustomTemplateView):
    template_name = "contact_us.html"


class UnderConstructionView(CustomTemplateView):
    template_name = "under_construction.html"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")


@method_decorator(login_required, name="dispatch")
class UserHomeView(CustomTemplateView):
    template_name = "user_home.html"


### MODULES ###
# Company #
@method_decorator(login_required, name="dispatch")
class CompanyView(CustomTemplateView):
    template_name = "modules/company.html"

    def dispatch(self, request, *args, **kwargs):
        """overriding dispatch
        - If the user isn't authenticated, it doesn't do any of these checks and
        the request is dispatched normally.
        - If the user is authenticated, the method tries to get a social_account
        that's associated with this use.
           = Then it tries to get a CompanySocialAccount that's associated with
           the social_account.
           = If the CompanySocialAccount doesn't exist or the associated company
           field in company_social_account is None, it will redirect the user to
           the "user_home" page.

         If everything is fine (i.e., the user is authenticated, the
         CompanySocialAccount exists and the associated company field is not None),
         it continues to dispatch the request normally.
        """
        if self.request.user.is_authenticated:
            try:
                social_account = self.request.user.socialaccount_set.get(
                    provider=self.provider_name
                )
                company_social_account = CompanySocialAccount.objects.get(
                    social_account=social_account
                )
                if company_social_account.company is None:
                    return redirect("user_home")
            except CompanySocialAccount.DoesNotExist:
                return redirect("user_home")
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """Multi Forms handler
        update form for each field then create to add new fields
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
            logger.info(request.POST)

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

            logger.info(request.POST)

        # Delete form
        elif form_type == "delete_driver":
            driver_id = request.POST.get("driver_id")
            driver = Drivers.objects.get(id=driver_id)
            driver.delete()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            social_account = self.request.user.socialaccount_set.get(
                provider=self.provider_name
            )
            company_social_account = CompanySocialAccount.objects.get(
                social_account=social_account
            )
            context["company"] = company_social_account.company
            context["drivers"] = Drivers.objects.filter(
                company=company_social_account.company
            )
            context["create_form"] = CreateDriverForm(prefix="create")
            context["update_form"] = UpdateDriverForm(prefix="update")
            context["delete_form"] = DeleteDriverForm(prefix="delete")
        return context


# Vehicles #
@method_decorator(login_required, name="dispatch")
class VehiclesView(CustomTemplateView):
    logger.debug('VehicleView hit')
    template_name = "modules/vehicles.html"

    def post(self, request, *args, **kwargs):
        # Create and update form for tractors
        form_type = request.POST.get("form_type")
        logger.debug(form_type)
        if form_type == "create_tractor":
            form = TractorForm(request.POST)
            if form.is_valid():
                tractor = form.save(commit=False)
                tractor.company = self.get_company(request.user, self.provider_name)
                tractor.domain 
                tractor.save()
                return redirect("vehicles")
            else:
                logger.error(form.errors)
            logger.info(request.POST)

        elif form_type == "update_tractor":
            tractor_id = request.POST.get("tractor_id")
            tractor = Tractors.objects.get(id=tractor_id)
            form = TractorForm(request.POST, instance=tractor)
            if form.is_valid():
                form.save()
                return redirect("vehicles")
            else:
                logger.error(form.errors)

            logger.info(request.POST)

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
            logger.info(request.POST)

        elif form_type == "update_trailer":
            trailer_id = request.POST.get("trailer_id")
            trailer = Trailers.objects.get(id=trailer_id)
            form = TrailerForm(request.POST, instance=trailer)
            if form.is_valid():
                form.save()
                return redirect("vehicles")
            else:
                logger.error(form.errors)

            logger.info(request.POST)

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            social_account = self.request.user.socialaccount_set.get(
                provider=self.provider_name
            )
            company_social_account = CompanySocialAccount.objects.get(
                social_account=social_account
            )
            context["company"] = company_social_account.company
            context["tractors"] = Tractors.objects.filter(
                company=company_social_account.company
            )
            context["trailers"] = Trailers.objects.filter(
                company=company_social_account.company
            )
            context["create_tractor_form"] = TractorForm(prefix="create")
            context["update_tractor_form"] = TractorForm(prefix="update")
            context["create_trailer_form"] = TrailerForm(prefix="create")
            context["update_trailer_form"] = TrailerForm(prefix="update")
        return context


@method_decorator(login_required, name="dispatch")
class OrdersView(CustomTemplateView):
    template_name = "modules/orders.html"


@method_decorator(login_required, name="dispatch")
class TicketsView(CustomTemplateView):
    template_name = "modules/tickets.html"


@method_decorator(login_required, name="dispatch")
class CashTransferView(CustomTemplateView):
    template_name = "modules/cashtransfer.html"


### Helpers ###
def get_provider_id(user, provider_name):
    """get provider id from social account, required to retrieve
    image from social nets
    """
    try:
        social_account = user.socialaccount_set.get(provider=provider_name)
        logger.debug(type(social_account.get_provider().id))
        return social_account.get_provider().id
    except user.socialaccount_set.model.DoesNotExist:
        return None
