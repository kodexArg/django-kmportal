from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.views.helpers import CustomTemplateView


@method_decorator(login_required, name="dispatch")
class ExtraCashView(CustomTemplateView):
    template_name = "modules/extracash.html"