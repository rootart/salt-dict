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
BASE_DIR = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(BASE_DIR, 'apps'),)



LOCAL_TEMPLATE_CONTEXT_PROCESSORS_PREFIX = LOCAL_TEMPLATE_CONTEXT_PROCESSORS = LOCAL_MIDDLEWARE_CLASSES_PREFIX = LOCAL_MIDDLEWARE_CLASSES = LOCAL_INSTALLED_APPS_PREFIX = LOCAL_INSTALLED_APPS = ()



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+snu2+2vc*)0xxc^0ysbs56fi+w-p-@rtooz12u3iz_rfqelpr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dictionary',
    'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'salt.urls'

WSGI_APPLICATION = 'salt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'


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

