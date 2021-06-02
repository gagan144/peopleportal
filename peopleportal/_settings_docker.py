from peopleportal.settings_common import *


# read environment variables
ENV_SECRET_KEY = os.environ['PP_SECRET_KEY']
ENV_DEBUG = bool(int( os.environ['PP_DEBUG'] ))
ENV_PG_HOST = os.environ['PP_PG_HOST']
ENV_PG_PORT = os.environ['PP_PG_PORT']
ENV_PG_USERNAME = os.environ['PP_PG_USERNAME']
ENV_PG_PASSWORD = os.environ['PP_PG_PASSWORD']
ENV_PG_DBNAME = os.environ['PP_PG_DBNAME']



# SECURITY WARNING: keep the secret key used in production secret!
# Code:
#   from django.utils.crypto import get_random_string
#   get_random_string(50, 'abcdefghijklmnopqrstuvwxyz0123456789!@#%^&*(-_=+)')
SECRET_KEY = ENV_SECRET_KEY


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENV_DEBUG

ALLOWED_HOSTS = ["*"]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': ENV_PG_DBNAME,
        'USER': ENV_PG_USERNAME,
        'PASSWORD': ENV_PG_PASSWORD,
        'HOST': ENV_PG_HOST,
        'PORT': ENV_PG_PORT
    }
}
