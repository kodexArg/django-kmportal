from loguru import logger as log
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.utils.translation import gettext as _
from django.views import View
from django.views.generic import TemplateView

from app.models import CompanySocialAccount


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
        return context


@method_decorator(login_required, name="dispatch")
class DriversView(CustomTemplateView):
    template_name = "modules/drivers.html"


@method_decorator(login_required, name="dispatch")
class OrdersView(CustomTemplateView):
    template_name = "modules/orders.html"


@method_decorator(login_required, name="dispatch")
class TicketsView(CustomTemplateView):
    template_name = "modules/tickets.html"


@method_decorator(login_required, name="dispatch")
class CashTransferView(CustomTemplateView):
    template_name = "modules/cashtransfer.html"


@method_decorator(login_required, name="dispatch")
class VehiclesView(CustomTemplateView):
    template_name = "modules/vehicles.html"


### Helpers ###
def get_provider_id(user, provider_name):
    """get provider id from social account, required to retrieve
    image from social nets
    """
    try:
        social_account = user.socialaccount_set.get(provider=provider_name)
        log.debug(type(social_account.get_provider().id))
        return social_account.get_provider().id
    except user.socialaccount_set.model.DoesNotExist:
        return None
