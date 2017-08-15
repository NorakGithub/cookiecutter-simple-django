from .base import *

# Disable debug mode in production
DEBUG = False

# Django secret key
# TODO: Change to your own key
SECRET_KEY = 'CHANGE_ME!!'

# Allowed host
# TODO: Change to host that allowed
ALLOWED_HOSTS = ['*']

# Production environment apps
INSTALLED_APPS += [
    's3_folder_storage',
    'collectfast'
]

# Database url
# TODO: Change to your database URL
DATABASES = {
    'default': env.db('DATABASE_URL', default='postgres://postgres:postgres@localhost:5432/postgres')
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# S3 Credential
# TODO: Update your S3 credential
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''

STATIC_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/"
MEDIA_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/"

# HTTPS Configuration
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
