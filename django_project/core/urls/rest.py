from django.urls import path
from django.conf.urls import include
from rest_framework import routers

app_name = "rest"

v1_router = routers.DefaultRouter()


urlpatterns = [
    # API views
    path("", include(v1_router.urls)),
    path("v1/", include(v1_router.urls)),
]
