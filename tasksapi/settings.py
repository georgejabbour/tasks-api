from datetime import timedelta
import os
from pathlib import Path
from dotenv import load_dotenv
import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

env = environ.Env(DEBUG=(bool, False))
env_file = os.path.join(BASE_DIR, ".env")
ON_RAILWAY = env('ON_RAILWAY', default=False)
if not ON_RAILWAY and os.path.isfile(env_file):
    env.read_env(env_file)
ENV_ROLE = os.getenv('ENV_ROLE', default='local')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    'https://jabbour-tasks.vercel.app/',
    'jabbour-tasks.vercel.app',
    'https://django-server-production-155b.up.railway.app/',
    'django-server-production-155b.up.railway.app'
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_HEADERS = [
    "x-api-key",
    "content-type",
    "origin",
    "accept",
    "x-csrftoken",
    "x-requested-with",
    "Authorization",
    'client-id'
]

CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
    'https://jabbour-tasks.vercel.app/',
    'https://django-server-production-155b.up.railway.app/'
]

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

INSTALLED_APPS = [
    'tasks',
    'whitenoise',
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"

# Use your custom authentication backend
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'tasks.authentication.SessionTokenAuthentication',
    )
}

AUTH_USER_MODEL = 'tasks.User'

AUTHENTICATION_BACKENDS = [
    'tasks.authentication.SessionTokenAuthentication',
    # Keep the default model backend for admin access
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'tasksapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tasksapi.wsgi.application'

DATABASES = {
    'default': env.db('DATABASE_URL')
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
