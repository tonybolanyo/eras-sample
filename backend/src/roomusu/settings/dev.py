"""
Settings for dev environment
"""

import logging
import os

from .base import *  # pylint: disable=W0401, W0614

logger = logging.getLogger(__file__)

DEBUG = True
PRODUCTION = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

SECRET_KEY = os.environ.get('SECRET_KEY', SECRET_KEY)

ADMINS = (
    (
        os.environ.get('ADMIN_EMAIL_NAME', ''),
        os.environ.get('ADMIN_EMAIL_ADDRESS', ''),
    ),
)

STATIC_ROOT = os.path.join(BASE_DIR, os.environ.get('STATIC_ROOT', "static/"))
STATIC_URL = os.environ.get('STATIC_URL', "/assets/")

MEDIA_ROOT = os.path.join(BASE_DIR, os.environ.get('MEDIA_ROOT', "media/"))
MEDIA_URL = os.environ.get('MEDIA_URL', "/media/")

MIDDLEWARE += [
    'django.middleware.locale.LocaleMiddleware',
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'SQL_ENGINE', 'django.db.backends.postgresql_psycopg2'
        ),
        'NAME': os.environ.get('DB_DATABASE', 'postgres'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 5432),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'postgres'),
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue'}
    },
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(module)s '
            '(%(filename)s %(lineno)d): %(message)s'
        },
        'simple': {
            'format': '[%(levelname)s] (%(filename)s %(lineno)d): %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'feed': {'handlers': ['console'], 'level': 'INFO', 'propagate': True},
        'rest_framework': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


# Activate to inspect generated SQL from Django ORM
if os.environ.get('DEBUG_SQL', 'False') == 'True':
    DEBUG_SQL = {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
    LOGGING['loggers'].update(DEBUG_SQL)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
