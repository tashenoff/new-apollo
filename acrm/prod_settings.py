import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'django-insecure-c7*#6@p6+p^eSDArfoblh!^nledk!bwy4f@f5x%08%kw+o@n2'

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'apollo.kz', 'www.apollo.kz','crm.apollo.kz']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'apollo_db',
        'USER': 'apollo_db_admin',
        'PASSWORD': 'ESQzD3rLK1v',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

