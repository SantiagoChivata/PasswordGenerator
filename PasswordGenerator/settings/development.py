import os
from dotenv import load_dotenv
from PasswordGenerator.settings.base import *


load_dotenv(Path.joinpath(BASE_DIR,'.env'))

SECRET_KEY = os.environ.get('SECRET_KEY')

#  SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
