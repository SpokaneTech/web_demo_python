from .gui import urlpatterns as gui_urls
from .list import urlpatterns as list_urls
from .rest import urlpatterns as rest_urls

app_name = "main_app"

urlpatterns = rest_urls + gui_urls + list_urls
