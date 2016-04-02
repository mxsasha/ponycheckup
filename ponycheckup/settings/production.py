from .base import *

SECRET_KEY = get_env_variable("SECRET_KEY")

ALLOWED_HOSTS = ('.ponycheckup.com', )

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_env_variable("DB_NAME"),
        'USER': get_env_variable("DB_USERNAME"),
        'PASSWORD': get_env_variable("DB_PASSWORD")
    }
}

