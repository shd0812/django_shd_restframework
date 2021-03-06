"""
Django settings for api_platform project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import datetime
from pathlib import Path
import sys, os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nuv9857rbbw%=$k^vlqdoklw9)0u(pp76tp4v(yy6tt$!qry#l'

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

    'rest_framework',
    'drf_yasg',

    'users.apps.UsersConfig',
    'projects.apps.ProjectsConfig',
    'interfaces.apps.InterfacesConfig',
    'debugtalks.apps.DebugtalksConfig',
    'configures.apps.ConfiguresConfig',
    'reports.apps.ReportsConfig',
    'testcases.apps.TestcasesConfig',
    'testsuits.apps.TestsuitsConfig',
    'envs.apps.EnvsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'api_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'api_platform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'api',
        'HOST': '122.51.192.201',
        'PORT': 3367,
        'USER': 'root',
        'PASSWORD': 'ilrssw'
    }
}


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
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=50),
    'JWT_RESPONSE_PAYLOAD_HANDLER':
        'users.utils.jwt_handler.jwt_response_payload_handler',
}
REST_FRAMEWORK = {
    'DATETIME_FORMAT': '%Y-%m%d %H:%M:%S', #设置时间格式
    'LANGUAGE_CODE': 'zh-hans',
    'TIME_ZONE': 'Asia/Shanghai',

    "DEFAULT_AUTHENTICATION_CLASSES": [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        # "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
                                        ],

    'DEFAULT_PAGINATION_CLASS': 'utils.pagenations.MyPageNumberPagination',
    'PAGE_SIZE': 5,

    # "DEFAULT_PERMISSION_CLASSES" : ["apps.users.auth.authenticate.AuthTicate", ],
    # "DEFAULT_THROTTLE_RATES": {
    # "luffy": "3/m"
    #  }
    # "DEFAULT_VERSION": "v1",
    # "ALLOWED_VERSIONS": ['v1', 'v2'],
    # "VERSION_PARAM": 'version',
    # "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.URLPathVersioning",
    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',

}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

