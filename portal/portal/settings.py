#ping
import os
import dotenv
from pathlib import Path
from .custom_storage import DocumentStorage

dotenv.load_dotenv()
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("SECRETKEY")
DEBUG = False if os.environ.get("DEBUG") == "False" else True

ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    "django.contrib.humanize",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "storages",  # s3 bucket (django-storages)
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.facebook",
    "sslserver",  # django-sslserver
    "compressor",  # compressor
    "rest_framework",  # rest
    "api",
    "tailwind",
    "theme",
    "django_browser_reload",  # reloader
    "app",
    "staff",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # compressor
    "django.middleware.security.SecurityMiddleware",  # compressor
    "django_browser_reload.middleware.BrowserReloadMiddleware",  # reloader
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

SESSION_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ['https://portal-km1151.grupo-avs.com', 'http://localhost:8000']

#SECURE_SSL_REDIRECT = True
#SECURE_HSTS_SECONDS = 3600  # 1 hour
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True
#SECURE_HSTS_PRELOAD = True

ROOT_URLCONF = "portal.urls"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n"
                # ... no... solo tarde 10 horas en darme cuenta del i18n missing...
                # para el gabo del futuro: NO USAR IA PARA CONFIGURACIONES DURAS
            ],
        },
    },
]

WSGI_APPLICATION = "portal.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.environ.get("MYSQL_DDBB"),
        "USER": os.environ.get("MYSQL_USER"),
        "PASSWORD": os.environ.get("MYSQL_PASS"),
        "HOST": os.environ.get("MYSQL_HOST"),
        "PORT": os.environ.get("MYSQL_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

SOCIAL_ACCOUNT_ADAPTER = "app.adapters.CustomAdapter"



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

COMPRESS_ENABLED = True

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder"
)

# Allauth configuration
# https://django-allauth.readthedocs.io/en/latest/configuration.html


SOCIALACCOUNT_LOGIN_ON_GET = True

SOCIAL_ACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {"access_type": "online"},
    }
}

# Lol... wtf... I hate you allauth. This can be found in the database.
SITE_ID = int(os.environ.get("SITE_ID"))

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# this doesn't work for 'staff' app
LOGIN_REDIRECT_URL = "user_home"

ACCOUNT_AUTHENTICATION_METHOD = "username"

# More Allauth configs...
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_EMAIL_VERIFICATION = "none"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "es"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
USE_I18N = True
LOCALE_PATHS = [BASE_DIR / "locale"]
USE_THOUSAND_SEPARATOR = False 

from django.conf.global_settings import LANGUAGES

LANGUAGES = [
    ("en", "English"),
    ("es", "Español"),
    ("pt", "Portuguêse"),
]


# TAILWIND and RELOADER
TAILWIND_APP_NAME = "theme"

INTERNAL_IPS = [
    "127.0.0.1",
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
AWS_ACCESS_KEY_ID = os.environ.get("AWS_KEY")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SEC")
AWS_STORAGE_BUCKET_NAME = "portal-km1151"

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

AWS_STATIC_LOCATION = "static/document"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/document/"

DEFAULT_FILE_STORAGE = '.custom_storage.DocumentStorage'


STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]

STATIC_ROOT = BASE_DIR.parent / "local-cdn" / "static"  # stored for production

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
