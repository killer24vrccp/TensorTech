from constance import config
from django.utils.timezone import datetime


def context_processor(requests):
    context = {
        'app_name': config.SITE_TITLE,
        'copyright': datetime.now().year,
    }

    return context
