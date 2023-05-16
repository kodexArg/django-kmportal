from loguru import logger as log
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    log.debug(f"request.method: {request.method}")

    if request.method == "GET":
        form = UserCreationForm()
        return render(request, "registration/signup.html", {"form": form})

    elif request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:

            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
