from django.apps import AppConfig


class DevsConfig(AppConfig):
    name = 'devs'
    def ready(self):
        import devs.signals
