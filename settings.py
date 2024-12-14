import os
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Security settings (add these for security)
SECRET_KEY = env('SECRET_KEY', default='your-default-secret-key')
DEBUG = env.bool('DEBUG', default=True)

# Database configuration using environment variables
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='3306'),
    }
}

# Add CORS Headers
CORS_ALLOW_ALL_ORIGINS = True

# REST Framework Configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# Add Celery settings
CELERY_BROKER_URL = 'amqp://localhost'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

# Swagger setup with drf-yasg
INSTALLED_APPS = [
    # other apps
    'rest_framework',
    'corsheaders',
    'listings',
    'drf_yasg',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # other middlewares
]

# Add the static file settings
STATIC_URL = '/static/'

# Other settings...

