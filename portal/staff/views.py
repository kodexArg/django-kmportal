from loguru import logger
from app.views.helpers import CustomTemplateView
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.views import View
from staff.forms import CustomLoginForm


### UNAUTHORIZED PAGES ###
class StaffHomeView(View):
    template_name = "staff/home.html"

    def get(self, request):
        form = CustomLoginForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("staff_home")
            else:
                logger.error(request, "Invalid username or password.")
        else:
            logger.error(request, "Invalid username or password.")
        return render(request, self.template_name, {"form": form})
