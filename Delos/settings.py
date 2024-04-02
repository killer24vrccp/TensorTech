from django.utils.translation import gettext_lazy as _
from pathlib import Path
from constance import config
import psutil
import platform


LOCAL_OS = platform.uname()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t(6$c+j5es5a(58nu#hf3#c0iqh85_f)89#l0gz2@lzk0zueo*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DATA_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024  # 50Mb

ALLOWED_HOSTS = ['localhost']

# Application definition

SHARED_APPS = (
    "django_tenants",

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'crispy_forms',
    'crispy_bootstrap5',
    'betterforms',
    'django_countries',
    'constance',
    'constance.backends.database',

    'authentication',
    'webcore',
    'customers',
)

TENANT_APPS = (
    'app.todo',
)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
TENANT_MODEL = 'customers.Tenant'
TENANT_DOMAIN_MODEL = 'customers.Domain'
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True
PUBLIC_SCHEMA_URLCONF = 'Delos.urls_public'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Delos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Delos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'ttl',
        'USER': 'postgres',
        'PASSWORD': 'Ezeflow2024$',
        'HOST': '192.1.1.84',
        'PORT': '5432'
    }
}

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGE = (
    ('en', _('English')),
    ('fr', _('French')),
)

TIME_ZONE = 'America/Toronto'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# account and user settings
AUTH_USER_MODEL = 'authentication.User'
SESSION_COOKIE_AGE = 87000

CONSTANCE_CONFIG = {
    'SITE_TITLE': ('My Site', _('Site Title of your site')),
}

CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
