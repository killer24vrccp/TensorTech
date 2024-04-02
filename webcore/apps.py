from django.utils.translation import gettext_lazy as _
from django.apps import AppConfig


class WebcoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'webcore'
    verbose_name = _('WebCore')
