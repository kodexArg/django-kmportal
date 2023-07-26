from app.views.helpers import CustomTemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


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
        was_user_staff = request.user.is_staff
        logout(request)
        if was_user_staff:
            return redirect('staff_home')
        else:
            return redirect('home')
