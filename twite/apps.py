from django.apps import AppConfig


class TwiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'twite'

    def ready(self):
        import twite.signals
