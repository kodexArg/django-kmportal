import os
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

# replace 'portal.settings' with your settings module path if different
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portal.settings")

application = get_wsgi_application()
application = WhiteNoise(
    application,
    root=os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "local-cdn",
        "static",
    ),
)
