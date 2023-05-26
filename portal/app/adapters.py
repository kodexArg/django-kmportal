from django.contrib.auth.models import User
from allauth.account.models import EmailAddress
from allauth.exceptions import ImmediateHttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class CustomAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        """
        Invoked just after a user successfully authenticates via a
        social provider, but before the login is actually processed
        (and before the pre_social_login signal is emitted).

        We're trying to solve different use cases:
        - social account already exists, just go on
        - social account has no email or email is unknown, just go on
        - social account's email exists, link social account to existing user
        """

        # Ignore existing social accounts, just do this stuff for new ones
        if sociallogin.is_existing:
            return

        # some social logins don't have an email address, e.g. facebook accounts
        # with mobile numbers only, but allauth takes care of this case so just
        # ignore it
        if 'email' not in sociallogin.account.extra_data:
            return

        # check if given email address already exists.
        # Note: __iexact is used to ignore cases
        try:
            email = sociallogin.account.extra_data['email'].lower()
            email_address = EmailAddress.objects.get(email__iexact=email)

        # if it does not, let allauth take care of this new social account
        except EmailAddress.DoesNotExist:
            return

        # if it does, bounce back to the login page
        account = User.objects.get(email=email).socialaccount_set.first()
        messages.error(request, "A "+account.provider.capitalize()+" account already exists associated to "+email_address.email+". Log in with that instead, and connect your "+sociallogin.account.provider.capitalize()+" account through your profile page to link them together.")       
        raise ImmediateHttpResponse(redirect('/accounts/login'))