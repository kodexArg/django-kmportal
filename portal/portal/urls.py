from allauth.account.views import LoginView
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

# 'app' views
from app.views.authorized import UserHomeView
from app.views.fuel_orders import FuelOrderDataView, FuelOrderListView, FuelOrderViewPause, FuelOrderViewNewOrEdit
from app.views.extracash import ExtraCashView
from app.views.helpers import get_qr, get_server_time
from app.views.modules import CompanyView, VehiclesView
from app.views.unauthorized import AboutUsView, ContactUsView, HomeView, LogoutView, UnderConstructionView

# 'staff' views
from staff.views import StaffHomeView
from staff.forms import CustomLoginForm

# Without Internationalization
urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("accounts/", include("allauth.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("under_construction/", UnderConstructionView.as_view(), name="under_construction"),
    path("get_qr/<int:order_id>/", get_qr, name="get_qr"),
    path("get-server-time/", get_server_time, name="get-server-time"),
    path("orders/<int:order_id>/data/", FuelOrderDataView.as_view(), name="order_data"),
    path("orders/<int:order_id>/pause/", FuelOrderViewPause.as_view(), name="pause_order"),
]

# Staff Area without internationalization
urlpatterns += [
    path("staff/", StaffHomeView.as_view(), name="staff_home"),
    path("staff/login/", auth_views.LoginView.as_view(template_name="staff/login.html", form_class=CustomLoginForm), name="staff_login"),
    path("staff/logout/", auth_views.LogoutView.as_view(), name="staff_logout"),
]

# API Rest Framework
urlpatterns += [
    # path("api/", include("app.api.urls")),
]

# Internationalization
urlpatterns += i18n_patterns(
    path("", HomeView.as_view(), name="home"),
    path("about_us/", AboutUsView.as_view(), name="about-us"),
    path("contact_us/", ContactUsView.as_view(), name="contact-us"),
    path("user_home/", UserHomeView.as_view(), name="user_home"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("__reload__/", include("django_browser_reload.urls")),
    path("company/", CompanyView.as_view(), name="company"),
    path("vehicles/", VehiclesView.as_view(), name="vehicles"),
    path("orders/", FuelOrderListView.as_view(), name="orders"),
    path("orders/new/", FuelOrderViewNewOrEdit.as_view(), name="new_order"),
    path("orders/<int:order_id>/edit/", FuelOrderViewNewOrEdit.as_view(), name="edit_order"),
    path("tickets/", UnderConstructionView.as_view(), name="tickets"),
    path("extracash/", ExtraCashView.as_view(), name="extracash"),
)

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
