from peopleportal.settings_common import *


# SECURITY WARNING: keep the secret key used in production secret!
# Code:
#   from django.utils.crypto import get_random_string
#   get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)')
SECRET_KEY = "--- 50 letter key ----"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "--- pg dbname ---",
        'USER': "--- pg username ---",
        'PASSWORD': "--- pg password ---",
        'HOST': "127.0.0.1",
        'PORT': 5432
    }
}
