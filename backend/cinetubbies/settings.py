"""
Django settings for cinetubbies project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '33yo6x$&ogd%0w+gs+c96a4lqciu@w5=kkw50==3-aqqqnkt&v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'corsheaders',
  'authentication',
  'theaters',
  'movies',
  'media_upload',
  'fan_zone',
  'showtimes',
  'reservations'
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = (
  'DELETE',
  'GET',
  'OPTIONS',
  'PATCH',
  'POST',
  'PUT',
)
CORS_ALLOW_HEADERS = (
  '*'
)

ROOT_URLCONF = 'cinetubbies.urls'

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

WSGI_APPLICATION = 'cinetubbies.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
  # 'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'cinetubbies',
    'USER': 'root',
    'PASSWORD': 'password',
    'HOST': 'localhost',
    'PORT': '3306',
  },

  # for unit tests
  # 'default': {
  #   'ENGINE': 'django.db.backends.sqlite3',
  #   'NAME': 'mydatabase'
  # }
}

# REST framework settings

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': (
    'rest_framework.permissions.IsAuthenticated',
  ),
  'DEFAULT_AUTHENTICATION_CLASSES': (
    'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    'rest_framework.authentication.SessionAuthentication',
    'rest_framework.authentication.BasicAuthentication',
  ),
}


# JWT settings

JWT_AUTH = {
  'JWT_ENCODE_HANDLER':
  'rest_framework_jwt.utils.jwt_encode_handler',

  'JWT_DECODE_HANDLER':
  'rest_framework_jwt.utils.jwt_decode_handler',

  'JWT_PAYLOAD_HANDLER':
  'rest_framework_jwt.utils.jwt_payload_handler',

  'JWT_PAYLOAD_GET_USER_ID_HANDLER':
  'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

  'JWT_RESPONSE_PAYLOAD_HANDLER':
  'authentication.utils.auth.jwt_response_payload_handler',

  'JWT_SECRET_KEY': SECRET_KEY,
  'JWT_GET_USER_SECRET_KEY': None,
  'JWT_PUBLIC_KEY': None,
  'JWT_PRIVATE_KEY': None,
  'JWT_ALGORITHM': 'HS256',
  'JWT_VERIFY': True,
  'JWT_VERIFY_EXPIRATION': True,
  'JWT_LEEWAY': 0,
  'JWT_EXPIRATION_DELTA': datetime.timedelta(days=150),
  'JWT_AUDIENCE': None,
  'JWT_ISSUER': None,

  'JWT_ALLOW_REFRESH': False,
  'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

  'JWT_AUTH_HEADER_PREFIX': 'JWT',
  'JWT_AUTH_COOKIE': None,
}

AUTH_USER_MODEL = 'authentication.User'

REST_USE_JWT = True

APPEND_SLASH = False


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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


# Email settings

EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')