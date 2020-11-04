from pathlib import Path
import os 
import django_heroku
import dj_database_url
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'youth/static/js', 'serviceworker.js')

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f8i9*367zexs(2y2w23jtdr71ob$&z4!y0=z+5yh1q@hky^-r4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    # third party apps
    'accounts',
    'bootstrap4',
    'youth',

    # newsletter apps
    'sorl.thumbnail',
    'newsletter',
    'pwa',

    # cleanup old pics after user changes them
    'django_cleanup.apps.CleanupConfig',
]

MIDDLEWARE = [
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 604800 			

ROOT_URLCONF = 'finances.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'finances.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


# Heroku Database Config

DATABASES={'default' : dj_database_url.config(conn_max_age=600)}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Media storage
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# AUTH redirect settings
LOGIN_REDIRECT_URL = "accounts:dashboard"
LOGOUT_REDIRECT_URL = "youth:index"

# Email settings



    # Home
    # About
    # Events
    # Sermons
    # Hello, Guest!


# django.contrib.sites settings
SITE_ID = 1 

# Activate Django-Heroku.
django_heroku.settings(locals())

options = DATABASES['default'].get('OPTIONS', {})
options.pop('sslmode', None)



# Dont confirm email before subscription
NEWSLETTER_CONFIRM_EMAIL = False

# Amount of seconds to wait between each email. Here 100ms is used.
NEWSLETTER_EMAIL_DELAY = 0.1

# Amount of seconds to wait between each batch. Here one minute is used.
NEWSLETTER_BATCH_DELAY = 60

# Number of emails in one batch
NEWSLETTER_BATCH_SIZE = 100

# paystack keys
PAYSTACK_PUBLIC_KEY='pk_live_6fd88f7a7e79d8ce558178692fab1f5e37293c5f',
PAYSTACK_SECRET_KEY='sk_live_be9332d2f408b2362c8afbbb3213c4d988b39312'

#SECURE_SSL_REDIRECT = True

# Google Cloud Storage
# STATICFILES_DIRS = [
#     "/home/ceasar/Desktop/Dev/finances/accounts/static/",
#     "/home/ceasar/Desktop/Dev/finances/newsletter/static/",
#     "/home/ceasar/Desktop/Dev/finances/youth/static/",
# ]
# DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# GS_BUCKET_NAME = 'youthchurch'
# STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
# STATIC_URL = 'https://storage.googleapis.com/youthchurch/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# from google.oauth2 import service_account
# GS_CREDENTIALS = service_account.Credentials.from_service_account_file(
#     '/home/ceasar/Downloads/youthchurch-293616-273cbcff4704.json' # see step 3
# )

# Cache Settings

