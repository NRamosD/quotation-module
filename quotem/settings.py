"""
Django settings for quotem project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

#from pathlib import Path
from decouple import config
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#Para REACT-->BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='')

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
    'apps.quote',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'django_filters'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'quotem.urls'
#os.path.join(BASE_DIR, 'templates/design/build'),
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR,'templates.quote')],
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

WSGI_APPLICATION = 'quotem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


""" DATABASES = {   #BD EXTERNA
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'quote',
        'USER' : config('SECRET_USER', default=''),
        'PASSWORD' : config('SECRET_PASS',default=''),
        'HOST' : config('SECRECT_HOST', default='localhost'),
        'PORT' : '3306',
        'OPTIONS': {
            'ssl': {'ca': 'BaltimoreCyberTrustRoot.crt.pem'}
        }
    }
} """
#contra bd nr 123.123-123.
DATABASES = {   #BD LOCAL
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'quote_local',
        'USER' : 'root',
        'PASSWORD' : '123.Contra.123', #No olviden dejar vacio este campo si no configuraron contraseña
        'HOST' : 'localhost',
        'PORT' : '3306',
        'OPTIONS': {
        }
    }
}










# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIR = [
    os.path.join(BASE_DIR, 'static'),
]
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'templates/design/build/static')
#]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#   
#Para la api
REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (       
       #'rest_framework_simplejwt.authentication.JWTAuthentication',
       'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.BasicAuthentication',
       'rest_framework.authentication.SessionAuthentication',
   ),
   #'DEFAULT_PERMISSION_CLASSES': (
    #    'rest_framework.permissions.IsAdminUser',
     #   'rest_framework.permissions.IsAuthenticated',
   #),
}
"""REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}"""
#para mi usuario
AUTH_USER_MODEL = 'quote.Users'

#para activar la cookie
REST_USE_JWT = True
JWT_AUTH_COOKIE = 'auth'

#Redirección
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

#corsheaders
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

"""
--------------------------------------------------------------------------------------------
https://docs.djangoproject.com/en/dev/howto/static-files/
DEPLOY STATIC FILES: https://docs.djangoproject.com/en/dev/howto/static-files/deployment/ --
--------------------------------------------------------------------------------------------
"""


#Dirección de archivos excel
#FILES_ROOT = os.path.join(BASE_DIR, 'Documentos')  #Serving static files during development
MEDIA_ROOT = os.path.join(BASE_DIR, 'files').replace('\\', '/') #folder
MEDIA_URL = '/Documents/' #url route
#MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "Documentos")
