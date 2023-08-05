from django.contrib.auth.backends import ModelBackend
from staff.models import PumpOperator
from loguru import logger

class PumpOperatorAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = PumpOperator.objects.get(username=username)
            logger.debug(f"Hashed Pass:  {user.password}")  # Log the hashed password
        except PumpOperator.DoesNotExist:
            logger.error(f"AuthenticationBackend error: User with username <{username}> not found")
            return None

        if not user.check_password(password):
            logger.error(f"AuthenticationBackend error: Incorrect password for user <{username}>")
            return None

        if not self.user_can_authenticate(user):
            logger.error(f"AuthenticationBackend error: User <{username}> is not allowed to authenticate (e.g., inactive or deleted)")
            return None

        return user
