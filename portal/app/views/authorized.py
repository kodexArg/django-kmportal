from django.shortcuts import redirect
from app.views.helpers import CustomTemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.decorators import method_decorator


@method_decorator(login_required, name="dispatch")
class UserHomeView(CustomTemplateView):
    template_name = "user_home.html"
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('staff_home')
        return super().dispatch(request, *args, **kwargs)


@method_decorator(login_required, name="dispatch")
class TicketsView(CustomTemplateView):
    template_name = "modules/tickets.html"



