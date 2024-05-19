import os

from django.apps import AppConfig


class ServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'service'

    def ready(self):
        if os.environ.get('RUN_MAIN'):
            from .startup import startup_routine
            startup_routine()
