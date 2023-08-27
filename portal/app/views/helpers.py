from io import BytesIO

from app.models import CompanySocialAccount, FuelOrders
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView
from loguru import logger
from qrcode import QRCode, constants
from qrcode.image import svg as qr_svg


class CustomTemplateView(TemplateView):
    """Used instead of TemplateView to add a custom context_data method"""

    provider_name = "Google"
    # context["provider_id"]

    def get_provider_id(self, user, provider_name):
        try:
            social_account = user.socialaccount_set.get(provider=provider_name)
            return social_account.get_provider().id
        except user.socialaccount_set.model.DoesNotExist:
            logger.error("Company does not exist")
            return None

    # context["company"]
    def get_company(self, user, provider_name):
        try:
            social_account = user.socialaccount_set.get(provider=provider_name)
            return social_account.companysocialaccount.company
        except (
            user.socialaccount_set.model.DoesNotExist,
            CompanySocialAccount.DoesNotExist,
        ):
            logger.error("Company does not exist")
            return None

    def get_company_id(self, user, provider_name):
        try:
            social_account = user.socialaccount_set.get(provider=provider_name)
            company_social_account = CompanySocialAccount.objects.get(social_account=social_account)
            return company_social_account.company.id
        except (
            user.socialaccount_set.model.DoesNotExist,
            CompanySocialAccount.DoesNotExist,
        ):
            logger.info("Company does not exist")
            return None

    # Context data getter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["provider_id"] = self.get_provider_id(self.request.user, self.provider_name)
            context["company"] = self.get_company(self.request.user, self.provider_name)
            context["user"] = self.request.user
        return context


# def get_provider_id(user, provider_name):
#     """get provider id from social account, required to retrieve
#     image from social nets
#     """
#     try:
#         social_account = user.socialaccount_set.get(provider=provider_name)
#         return social_account.get_provider().id
#     except user.socialaccount_set.model.DoesNotExist:
#         return None


def get_qr(request, operation_code):
    png_image = generate_qr_code_png(operation_code)
    response = HttpResponse(png_image, content_type="image/png")
    response["Content-Disposition"] = 'attachment; filename="qrcode.png"'
    return response

def generate_qr_code_png(text):
    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_stream = BytesIO()
    img.save(img_stream, format="PNG")
    img_string = img_stream.getvalue()
    return img_string


def generate_qr_code_svg(text):
    """returns a QR as a svg string from a given text"""

    qr = QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=100,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    factory = qr_svg.SvgImage
    svg_img = qr.make_image(image_factory=factory)
    svg_stream = BytesIO()
    svg_img.save(svg_stream)
    svg_string = svg_stream.getvalue().decode("utf-8")
    return svg_string


def get_server_time(request):
    now = timezone.now()
    return JsonResponse({"server_time": now.isoformat()})
