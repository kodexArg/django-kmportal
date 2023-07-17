from app.views.helpers import CustomTemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class UserHomeView(CustomTemplateView):
    template_name = "user_home.html"


@method_decorator(login_required, name="dispatch")
class TicketsView(CustomTemplateView):
    template_name = "modules/tickets.html"



