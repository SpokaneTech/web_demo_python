"""spokane_tech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import views
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import logout_then_login
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    # Django provided URLs
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", logout_then_login, name="logout"),
    # 3rd party URLs
    path("userextensions/", include("userextensions.urls")),
    path("handyhelpers/", include("handyhelpers.urls")),
    path("hostutils/", include("djangoaddicts.hostutils.urls")),
    path("pygwalker/", include("djangoaddicts.pygwalker.urls")),
    # RESTful API URLs
    path("rest/", include("core.urls.rest", namespace="rest")),
    path("rest/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("rest/swagger/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
    path("rest/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # URLs to local apps
    path("", views.Index.as_view(), name="index"),
    path("dashboard/", views.ProjectDashboard.as_view(), name="dashboard"),
    path("main_app/", include("main_app.urls", namespace="main_app")),
]

if settings.DEBUG:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
