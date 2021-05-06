from .base import *


INSTALLED_APPS += ['django_nose']

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--exe',
    '--verbosity=2',
    '--cover-erase',
    '--cover-html',
    '--cover-min-percentage=85',
    '--cover-package=talentx',
    '--rednose',
    '--force-color',
    '--with-doctest',
    # '--with-coverage',
    # '--cover-config-file=.coveragerc',
]

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get(
            'SQL_ENGINE', 'django.db.backends.postgresql_psycopg2'
        ),
        'NAME': 'postgres',  # os.environ.get('SQL_DATABASE', 'postgres'),
        'USER': 'postgres',  # os.environ.get('SQL_USER', 'postgres'),
        'HOST': 'localhost',  # os.environ.get('SQL_HOST', 'localhost'),
        'PORT': 5433,        # os.environ.get('SQL_PORT', 5432),
        'PASSWORD': 'postgres'  # os.environ.get('SQL_PASSWORD', 'postgres'),
    }
}
