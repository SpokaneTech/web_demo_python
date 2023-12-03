from django.apps import AppConfig


class App0Config(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "main_app"

    # def ready(self):
    #     import main_app.signals
