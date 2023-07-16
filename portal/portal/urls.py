"""
URL configuration for portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path("", views.home, name="home")
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path("", Home.as_view(), name="home")
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path("blog/", include("blog.urls"))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from app import views
from allauth.account.views import LoginView
from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from django.views.i18n import set_language
from app.views import (
    HomeView,
    AboutUsView,
    UserHomeView,
    CompanyView,
    ContactUsView,
    LogoutView,
    UnderConstructionView,
    FuelOrderListView,
    FuelOrderViewCancel,
    FuelOrderViewNewOrEdit,
    FuelOrderDataView,
    VehiclesView,
    get_qr,
    get_server_time,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("i18n/", include("django.conf.urls.i18n")),
    path("accounts/", include("allauth.urls")),
    path("login/", LoginView.as_view(), name="login"),
    path("under_construction/", UnderConstructionView.as_view(), name="under_construction"),
    path('get_qr/<int:order_id>/', views.get_qr, name='get_qr'),
    path('get-server-time/', get_server_time, name='get-server-time'),
    path('orders/<int:order_id>/data/', FuelOrderDataView.as_view(), name='order_data'),
    path("orders/<int:order_id>/cancel/", FuelOrderViewCancel.as_view(), name="cancel_order"),

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
    # Modules Pages
    path("__reload__/", include("django_browser_reload.urls")),
    path("company/", CompanyView.as_view(), name="company"),
    path("vehicles/", VehiclesView.as_view(), name="vehicles"),
    path("orders/", FuelOrderListView.as_view(), name="orders"),
    
    path("orders/new/", FuelOrderViewNewOrEdit.as_view(), name="new_order"),
    path("orders/<int:order_id>/edit/", FuelOrderViewNewOrEdit.as_view(), name="edit_order"),
    path("tickets/", UnderConstructionView.as_view(), name="tickets"),
    path("cashtransfer/", UnderConstructionView.as_view(), name="cashtransfer"),
)


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
