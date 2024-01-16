from django.conf.urls import include
from django.urls import path

# from main_app.views import rest
from rest_framework import routers

router = routers.DefaultRouter()


# main_app API Endpoints
# router.register(r"model_name", rest.ModelViewSet, "model_name")


urlpatterns = [
    # API views
    path("rest/", include(router.urls)),
]
