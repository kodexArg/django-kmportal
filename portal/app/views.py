from django.shortcuts import render

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.utils.translation import gettext as _
from django.utils.decorators import method_decorator

from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

class CustomTemplateView(TemplateView):
    provider_name = "Google"

    def get_provider_id(self, user, provider_name):
        try:
            social_account = user.socialaccount_set.get(provider=provider_name)
            return social_account.get_provider().id
        except user.socialaccount_set.model.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["provider_id"] = self.get_provider_id(
                self.request.user, self.provider_name
            )
        return context



class HomeView(CustomTemplateView):
    template_name = "home.html"


class AboutUsView(CustomTemplateView):
    template_name = "about_us.html"


class ContactUsView(CustomTemplateView):
    template_name = "contact_us.html"


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("home")

@method_decorator(login_required, name="dispatch")
class UserHomeView(CustomTemplateView):
    template_name = "user_home.html"


@method_decorator(login_required, name="dispatch")
class CompanyView(CustomTemplateView):
    template_name = "base/module/company.html"


@method_decorator(login_required, name="dispatch")
class DriversView(CustomTemplateView):
    template_name = "base/module/drivers.html"


@method_decorator(login_required, name="dispatch")
class OrdersView(CustomTemplateView):
    template_name = "base/module/orders.html"


@method_decorator(login_required, name="dispatch")
class TicketsView(CustomTemplateView):
    template_name = "base/module/tickets.html"


@method_decorator(login_required, name="dispatch")
class VehiclesView(CustomTemplateView):
    template_name = "base/module/vehicles.html"


### Code snippets ###
def welcome_card_html(request):
    return render(request, "welcome_card.html")


