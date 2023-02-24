from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class SummitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'summit'

    def ready(self):
        from . import updater
        updater.start()
        