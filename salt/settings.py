"""
Django settings for salt project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

import dj_database_url

BASE_DIR = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, 'apps'),)



LOCAL_TEMPLATE_CONTEXT_PROCESSORS_PREFIX = LOCAL_TEMPLATE_CONTEXT_PROCESSORS = LOCAL_MIDDLEWARE_CLASSES_PREFIX = LOCAL_MIDDLEWARE_CLASSES = LOCAL_INSTALLED_APPS_PREFIX = LOCAL_INSTALLED_APPS = ()


DATABASES = {'default': dj_database_url.config(default='postgres://rootart@localhost/mangalia_dev')}
DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'

SOUTH_DATABASE_ADAPTERS = {
    'default': 'south.db.postgresql_psycopg2'
}


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+snu2+2vc*)0xxc^0ysbs56fi+w-p-@rtooz12u3iz_rfqelpr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition
PROJECT_APPS = (
    'dictionary',
)
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'south',
    'tastypie',
    'tastypie_swagger',
    'haystack'
) + PROJECT_APPS

TASTYPIE_SWAGGER_API_MODULE = 'dictionary.api.v1_api'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

ROOT_URLCONF = 'salt.urls'

WSGI_APPLICATION = 'salt.wsgi.application'


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

TASTYPIE_DEFAULT_FORMATS = ['json',]

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'search_index'),
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

try:
    from settings_local import *
except ImportError:
    pass
else:
    TEMPLATE_CONTEXT_PROCESSORS = \
        LOCAL_TEMPLATE_CONTEXT_PROCESSORS_PREFIX + \
        TEMPLATE_CONTEXT_PROCESSORS + \
        LOCAL_TEMPLATE_CONTEXT_PROCESSORS
    MIDDLEWARE_CLASSES = \
        LOCAL_MIDDLEWARE_CLASSES_PREFIX + \
        MIDDLEWARE_CLASSES + \
        LOCAL_MIDDLEWARE_CLASSES
    INSTALLED_APPS = \
        LOCAL_INSTALLED_APPS_PREFIX + \
        INSTALLED_APPS + \
        LOCAL_INSTALLED_APPS

