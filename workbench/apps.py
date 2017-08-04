from django.apps import AppConfig


class WorkbenchConfig(AppConfig):

    name = 'workbench'

    def ready(self):
        import workbench.signals
