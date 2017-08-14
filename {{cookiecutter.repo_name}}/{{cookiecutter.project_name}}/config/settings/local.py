from .base import *

# Secret key doesn't matter in local development
SECRET_KEY = 'some-keys'

# Debug mode
DEBUG = True

# Allowed from all host
ALLOWED_HOSTS = ['*']

# App specifically for development
INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

# Middleware for development
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

# Database configuration
DATABASES = {
    'default': env.db("DATABASE_URL", default="postgres://postgres:postgres@localhost:5432/{{cookiecutter.database_name}}")
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# Django REST Framework Cors Header Origin
CORS_ORIGIN_ALLOW_ALL = True

# Static files
STATIC_ROOT = str(ROOT_DIR('static'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    str(ROOT_DIR.path('static_files')),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Media files
MEDIA_ROOT = str(ROOT_DIR('media'))
MEDIA_URL = '/media/'
