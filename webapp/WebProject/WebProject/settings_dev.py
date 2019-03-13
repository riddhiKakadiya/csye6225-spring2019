"""
Django settings for WebProject project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import configparser

try:
    HOSTNAME = socket.gethostname()
except:
    HOSTNAME = 'localhost'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#Get configuration from my.cnf
#Open and parse the file
config = configparser.ConfigParser()
pathToConfig = os.path.join(BASE_DIR, 'WebProject/config/my.cnf')
config.read(pathToConfig)

#Get configuration from my.cnf
#Open and parse the file
# config = configparser.ConfigParser()
# pathToConfig = os.path.join(BASE_DIR, 'WebProject/config/my.cnf')
# config.read(pathToConfig)
#Get variable

# S3_BUCKETNAME=config['S3']['bucketname']

# AWS_ACCESS_KEY_ID = config['AWS']['aws_access_key_id']
# AWS_SECRET_ACCESS_KEY = config['AWS']['aws_secret_access_key']

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l_k3zyn7$2j*vsvk&m3t5&*bp++r*=v*$c9gmoiy9z0xk5u_6m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Define whether to run in dev environment or default(local) environment
PROFILE = 'dev'

S3_BUCKETNAME = config['Config']['S3_BUCKET']

# Application definition

INSTALLED_APPS = [
    'user_auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_truncate',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user_auth.middleware.PutParsingMiddleware',
    'user_auth.middleware.JSONParsingMiddleware',
]

ROOT_URLCONF = 'WebProject.urls'

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

WSGI_APPLICATION = 'WebProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config['Config']['RDS_DB'],
        'USER': config['Config']['RDS_UN'],
        'PASSWORD': config['Config']['RDS_PASSWORD'],
        'HOST': config['Config']['RDS_HOST'],
        'PORT': 3306,
    }
}

#Password to Bcrypt
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        'OPTIONS': {
            'user_attributes': (
                'username', 'password'
            ),
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'EST'

USE_I18N = True

USE_L10N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'user_auth/attachments')
MEDIA_URL = '/attachments/'