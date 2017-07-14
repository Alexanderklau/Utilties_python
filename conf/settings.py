# -*- coding: utf-8 -*-

"""
Django settings for TkManager project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

import djcelery

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

BROKER_URL = "django://"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3564e^zg%sj9&o2v27)iw7r@8)pa8ozg@z-n72$$$h-khdy_pc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = False

TEMPLATE_DEBUG = True

USE_DATA_SERVER = True
#ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']
MIFAN_BLOCK_LIST = []

ORGANIZATION = 'test'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'kombu.transport.django',
    #'django_extensions',
    'django_gearman_commands',
    'corsheaders',
    'rest_framework',

    'business_manager.order',
    'business_manager.review',
    'business_manager.collection',
    'business_manager.custom',
    'business_manager.audit',
    'business_manager.juxinli',
    'business_manager.config_center',
    'business_manager.new_order',
    'business_manager.pc_reg',
    'business_manager.custom_command',
    'business_manager.merchant',
    'business_manager.employee',
    'business_manager.import_data',
    'business_manager.strategy',
    'business_manager.users',

    # 'debug_toolbar',
    # 'debug_panel',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'debug_panel.middleware.DebugPanelMiddleware',
)

ROOT_URLCONF = 'business_manager.urls'

WSGI_APPLICATION = 'business_manager.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cuishou',
        # 'NAME': 'dzh_tailong_test',
        # 'NAME': 'dzh_tl_test',
        # 'NAME': 'dzh_yjj_test',
        # 'NAME': 'dzh_bangfenqi',
        'USER': 'root',
        'PASSWORD':'123456',
        # 'PASSWORD': 'h7wFdCZN2NubZonbXAs1mYUf',
        # 'HOST': '114.55.125.148'
        # test
        'HOST': '127.0.0.1',


        # 'ENGINE': 'django.db.backends.mysql',
        # # 'NAME': 'saas_test2',
        # 'NAME': 'yijiejing_test',
        # # 'NAME': 'saas_multi_platform_test',
        # 'USER': 'rongshukeji',
        # 'PASSWORD': 'Rongshu_123',
        # 'HOST': 'rm-bp1i771wb378222ek.mysql.rds.aliyuncs.com',


        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'saas_multi_platform',
        # 'USER': 'dingdang',
        # 'PASSWORD': 'Dingdang123',
        # 'HOST': 'rm-bp1i771wb378222ek.mysql.rds.aliyuncs.com',
    }
}

MIFAN_DEBUG = True

REDIS = {
    "HOST" : "3d5ce3962104443f.m.cnhza.kvstore.aliyuncs.com",
    "PORT" : 6379,
    "AUTH" : "3d5ce3962104443f:Rongshu1234",
}

CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        # "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://{}@{}:{}/1".format(REDIS["AUTH"], REDIS["HOST"], REDIS["PORT"]),
        # "OPTIONS": {
            # "CLIENT_CLASS": "django_redis.client.DefaultClient",
        # }
    }
}



MONGO = {
        "HOST": "dds-bp1b7b44c70e94342.mongodb.rds.aliyuncs.com",
        "USER": "root",
        "DB": "",
        "PORT": 3717,
        "AUTH": "Rongshu1234",
}

MESSAGE_SERVER = {
    "HOST" : "127.0.0.1",
    "PORT" : 9104,
    "DEBUG" : True,
}

BANK_SERVER = {
    "HOST" : "127.0.0.1",
    "PORT" : 9102,
    "DEBUG" : True,
}

BIND_SERVER = {
    "HOST" : "127.0.0.1",
    "PORT" : 9103,
}

IP_SERVER = {
    "HOST" : "10.168.254.64",
    "PORT" : 9094,
}

LOG_SERVER = {
    "LOG_NAME": "tk_manager",
    "LOG_FILE": "tk_manager.log",
    "HOST" : "127.0.0.1",
    "PORT" : 9096,
}

RC_SERVER = {
    "HOST" : "10.168.254.64",
    "PORT" : 9095,
}

DATA_SERVER = {
    "ORG_NAME" : "dingdang",
    "URL" : "http://127.0.0.1:8888/query"
}

RISK_SERVER = {
    "HOST" : "127.0.0.1",
    # "PORT" : 39105,
    "PORT" : 8004,
}



USER_CENTER_SERVER = {
    'HOST': '127.0.0.1',
    'PORT': 8367,
}

WEB_HTTP_SERVER = {
    'HOST': '127.0.0.1',
    'PORT': 8368,
}

BUSINESS_PLATFORM = 'dev'
BUSINESS_PRODUCT = 'test_product'

IMAGE_SERVER_URL = 'http://127.0.0.1:8005/upload/bytes'

#using R or not
#USING_R = 1

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static/")

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    os.path.join(os.path.dirname(__file__),'static/').replace('\\','/'),
    os.path.join(os.path.dirname(__file__),'static/').replace('\\','/'),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__),'template').replace('\\','/'),
    # '/home/lau/rst_saas/nenv/lib/python2.7/site-packages/templates',
)

CORS_ORIGIN_ALLOW_ALL = False
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'google.com',
    '121.40.202.86:9094',
    '121.40.202.86:8006',
    '10.10.10.196:8020',
    '127.0.0.1:8020',
    '10.10.10.197:8020',
    '10.10.10.196:8020',
    '192.168.0.14:8020'
    #'182.148.35.29',
    #'182.149.194.220',
)


TEMPLATE_CONTEXT_PROCESSORS =(
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    )

#AUTH_USER_MODEL = 'TkManager.review.Employee'
LOGIN_REDIRECT_URL = '/'

#OSS_URL = 'http://tk-pic.oss-cn-hangzhou.aliyuncs.com/'
OSS_URL = 'http://tktest.oss-cn-hangzhou.aliyuncs.com/'

GEARMAN_SERVERS = ['127.0.0.1:4730']

JUXINLI_CONF =  {
    'org_name' : 'taikangjinrong',
    'client_secret' : '4ade042f9af2471d93268baed949a5e2',
    'access_report_data_api' : 'https://www.juxinli.com/api/access_report_data',
    'access_raw_data_api' : 'https://www.juxinli.com/api/access_raw_data',
    'access_report_token_api' : 'https://www.juxinli.com/api/access_report_token',
    'access_e_business_raw_data_api' : 'https://www.juxinli.com/api/access_e_business_raw_data',
}

DEBUG_TOOLBAR_PATCH_SETTINGS = False

IMPORT_FILE = ["import_data/3.xls"]#, "import_data/2.xls", "import_data/3.xls", "import_data/4.xls"]

# formal key
#CORPID = "MFG21b6sh4lFFIZC2j"
#TOKEN = "dzK5klI"
#ENCODINGAESKEY =  "zTKo235dYP2qOdqdEPKoDhlJxuuoLrXsEqbXNutHAWN"

# test key
TOKEN = "MyqcUA4"
ENCODINGAESKEY = "KWB3nDfmaXGqGPla3NMZ2eQzEDS0hJK5wLaeHH7ns0O"
CORPID = "test1XShXc8YkpO2yN"

#mifan test url:
#MIFAN_URL = "api.testmilijinfu.com"
#mifan formal url:
#MIFAN_URL = "api.milijinfu.com"

# init log
from business_manager.python_common.log_client import CommonLog as Log
import logging

host = LOG_SERVER["HOST"]
port = LOG_SERVER["PORT"]
name = LOG_SERVER["LOG_NAME"]
filename = LOG_SERVER["LOG_FILE"]
Log().init_log_include_local_file(name, "DEBUG", host, port, filename, 1024)
Log().info("init settings done.")

PUSH_SERVER = {"HOST": '127.0.0.1',
               "PORT": 9100
}

CELERY_BROKER = ''
CRON_TIME = 1
CELERY_BACKEND = ''

WEIXIN_PUSH_URL = 'http://devapiwap.hualahuala.com/web/push/authentication_notice'

LLD_Still_URL = 'http://dev.lanlingdai.net/lld-admin/app/business/payment/repay'

LLD_CHECK_URL = ''


BUSINESS_PLATFORM = 'dev'
BUSINESS_PRODUCT = 'test_product'

# IMAGE_SERVER_URL = 'http://127.0.0.1:8005/upload/bytes'
IMAGE_SERVER_URL = 'http://127.0.0.1:8005/upload/files'

BUSINESS_REPORT_REDIS = {
    'HOST': '3d5ce3962104443f.m.cnhza.kvstore.aliyuncs.com',
    'PASSWORD': '3d5ce3962104443f:Rongshu1234',
    'PORT': 6379,
    'DB': 4,
}

DATA_REPORT_SERVER = {
    'HOST': '121.40.196.233',
    'PORT': 8800,
    'REDIS': '3d5ce3962104443f.m.cnhza.kvstore.aliyuncs.com',
    'REDIS_PORT': '3d5ce3962104443f:Rongshu1234',
    'REDIS_AUTH': 6379,
    'REDIS_DB': 4,
}

REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
    'EXCEPTION_HANDLER': 'business_manager.import_data.services.cute_exception_handler',
    # 'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.FormParser'],

    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%Y-%m-%d %H:%M:%S',
}

# 数据导入预置字段模板
IMPORT_DATA = {
    "module_name": "import"
}

MEDIA_ROOT = BASE_DIR + "/media/"
MEDIA_URL = "media/"
ALLOW_VERIFY = True
ALLOW_DEDUCTIONS = True

DOMAIN = ''

ALLOW_DOWNLOAD_REPORT = True

REPORT_SERVER_HOST = ''
REPORT_SERVER_PORT = ''
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_AGE = 60 * 60


# DEBUG_TOOLBAR_PANELS = (
#     'debug_toolbar.panels.version.VersionDebugPanel',
#     'debug_toolbar.panels.timer.TimerDebugPanel',
#     'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
#     'debug_toolbar.panels.headers.HeaderDebugPanel',
#     'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
#     'debug_toolbar.panels.template.TemplateDebugPanel',
#     'debug_toolbar.panels.sql.SQLDebugPanel',
#     'debug_toolbar.panels.signals.SignalDebugPanel',
#     'debug_toolbar.panels.logger.LoggingPanel',
# )


# INTERNAL_IPS = ('127.0.0.1',)
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django.db.backends': {
#             'handlers': ['console'],
#             'level': 'DEBUG' if DEBUG else 'INFO',
#         },
#     },
# }