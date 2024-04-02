from constance import config


def context_processor(requests):
    context = {
        'app_name': config.SITE_TITLE
    }

    return context
