from django.contrib.messages import constants as message_constants
from django.contrib.messages import constants as messages
from decouple import config
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.twitter',
    'allauth.socialaccount.providers.facebook',
    'social_django',
]

CUSTOM_APPS = [
    'devs.apps.DevsConfig',
]

INSTALLED_APPS = THIRD_PARTY_APPS + CUSTOM_APPS + DEFAULT_APPS

SITE_ID = 1

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'APP': {
            'client_id': '123',
            'secret': '456',
            'key': ''
        }
    },
    'twitter': {
        'APP': {
            'client_id': '123',
            'secret': '457',
            'key': ''
        }
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'devtz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'devtz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Dar_es_Salaam'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = "devs.Dev"

# LOGIN_REDIRECT_URL = "login"

LOGOUT_REDIRECT_URL = 'home'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Messages
MESSAGE_LEVEL = message_constants.DEBUG

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3

ACCOUNT_EMAIL_VERIFICATION = True

# This will print email to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '152004136755226'
SOCIAL_AUTH_FACEBOOK_SECRET = '3f0014317aef5f8dad7948d4a5bc1258'

# Twitter
SOCIAL_AUTH_TWITTER_KEY = '5vmeb0RsZLQE2Sy8Wr9tI6MFQ'
SOCIAL_AUTH_TWITTER_SECRET = 'D55BfmxvJUVwId25OPzu5bocXxvuB4ePtRGakR2h7AtfTAJge4'
SOCIAL_AUTH_BEARIER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAA%2FuMwEAAAAAZ0ftv5BQ8RsLPWOtkSCrRyRHlHY%3DGYi5IZRKBsUHVXTvuoCfCN0bCyeRfw2QLYQFWvlYOQuY70noIG'

# Github
SOCIAL_AUTH_GITHUB_KEY = 'd48570bb143e58a4702f'
SOCIAL_AUTH_GITHUB_SECRET = '88540ecb5ff0d10edbe0d4dc52bde3007a4743fc'
