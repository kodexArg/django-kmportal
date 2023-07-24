from app.views.helpers import CustomTemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View


### UNAUTHORIZED PAGES ###
class StaffHomeView(CustomTemplateView):
    template_name = "staff/home.html"
