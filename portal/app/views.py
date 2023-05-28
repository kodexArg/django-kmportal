from loguru import logger as log
from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth import logout

from django.utils.translation import gettext as _

# Create your views here.


def home(request):
    context = {
        "get_provider_id": get_provider_id,
    }
    return render(request, "home.html", context)


def logout_view(request):
    log.debug("Logout")
    logout(request)
    return redirect("home")


# Code snippets
def welcome_card_html(request):
    return render(request, "welcome_card.html")


# Helpers
def get_provider_id(user, provider_name):
    """get provider id from social account, required to retrieve image from social net

    Args:
        user (_type_): _description_
        provider_name (_type_): "Google"

    Returns:
        _type_: provider id
    """
    try:
        social_account = user.socialaccount_set.get(provider=provider_name)
        log.debug(type(social_account.get_provider().id))
        return social_account.get_provider().id
    except user.socialaccount_set.model.DoesNotExist:
        return None
