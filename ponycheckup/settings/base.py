import os
from django.core.exceptions import ImproperlyConfigured
from unipath import Path

PROJECT_DIR = Path(__file__).ancestor(3)

DEBUG = False
TEMPLATE_DEBUG = False

ADMINS = (
    ('Sasha Romijn', 'github@mxsasha.eu'),
)
MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = "github@mxsasha.eu"

SITE_ID = 1

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
USE_I18N = False
USE_L10N = False
USE_TZ = False

MEDIA_ROOT = PROJECT_DIR.child("media")
MEDIA_URL = '/media/'

STATIC_ROOT = PROJECT_DIR.child("static")
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR.child("assets"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ponycheckup.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'ponycheckup.wsgi.application'

TEMPLATE_DIRS = (
    PROJECT_DIR.child("ponycheckup").child("templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)


INSTALLED_APPS = (
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_extensions',

    'ponycheckup.check',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)
