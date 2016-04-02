from .base import *

DEBUG = True
TEMPLATE_DEBUG = True
THUMBNAIL_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': PROJECT_DIR.child('db.sqlite'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_PORT = 2525
SECRET_KEY = 'm0qxmcn*j3_)))h4#bi71tn8zemagb&amyfil-@mu&3kxcu8%_'

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware', )

INSTALLED_APPS += (
    'debug_toolbar',
)