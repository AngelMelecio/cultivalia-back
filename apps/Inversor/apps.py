from django.apps import AppConfig


class InversorConfig(AppConfig):
    name = 'apps.Inversor'

    def ready(self):
        import apps.Inversor.signals