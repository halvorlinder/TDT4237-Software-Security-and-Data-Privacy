"""
Django settings for securehelp project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
import os.path

# The PRODUCTION variable decides how the static files are handeled in wsgi.py
# The variable is set to 'True' (string) when running with docker
PRODUCTION = os.getenv('PRODUCTION', False)

# Get environment variables
GROUP_ID = os.environ.get("GROUP_ID", "3000")
PORT_PREFIX = os.environ.get("PORT_PREFIX", "")
DOMAIN = os.environ.get("DOMAIN", "localhost")
PROTOCOL = os.environ.get("PROTOCOL", "http")

# Set Content Security Policy (CSP)
CSP_DEFAULT_SRC = ("'self'")
CSP_IMG_SRC = ("'self'")
CSP_STYLE_SRC = ("'self'")
CSP_SCRIPT_SRC = ("'self'")

# Set the URL used for redirecting
# URL in local development will not find environment variables and looks like: 'http://localhost:3000' (redirect to node)
# URL in local production with docker can look like this: 'http://localhost:21190', where 190 is the GROUP_ID
# URL in remote production with docker can look like this: 'http://molde.idi.ntnu.no:21190', where 190 is the GROUP_ID
URL = PROTOCOL + '://' + DOMAIN + ':' + PORT_PREFIX + GROUP_ID

# Email configuration
# The host must be running within NTNU's VPN (vpn.ntnu.no) to allow this config
# Usage: https://docs.djangoproject.com/en/3.1/topics/email/#obtaining-an-instance-of-an-email-backend
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.stud.ntnu.no"
EMAIL_USE_TLS = False
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = "tdt4237-group" + GROUP_ID + " " + "<noreply@idi.ntnu.no>"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

AUTH_USER_MODEL = "users.User"


SECRET_KEY = 'asdkjasdasd2-gmdf18+ep^k4d4)=uf%+1h$5(p5!l3-g24xb10^%5ycj9!dp37'

DEBUG = True

ALLOWED_HOSTS = [
    # Hosts for local development
    '127.0.0.1',
    'localhost',
    # Hosts for production
    'molde.idi.ntnu.no',
]

CORS_ALLOWED_ORIGINS = [
    # Allow requests from node app in development
    "http://localhost:3000",
    # Allow requests from node app in production
    "http://localhost:5000",
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'apps.users',
    'apps.certifications',
    'apps.help_requests'
]

MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'securehelp.urls'

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

WSGI_APPLICATION = 'securehelp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'


STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA FILES
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


PASSWORD_RESET_TIMEOUT = 3600  # Token valid for one hour

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60000),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
}
