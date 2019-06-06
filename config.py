# -*- coding: utf-8 -*-
from datetime import timedelta
DEBUG = False
SQLALCHEMY_ECHO = False
PER_PAGE = 32
UPLOAD_URL = 'app/static'
PREVIEW_THUMBNAIL = '-preview'
API_PREFIX = "/api"
LOGIN_TIME_OUT = 3600
CACHE_TYPE = "redis"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
JWT_AUTH_URL_RULE = "/api/login"
JWT_EXPIRATION_DELTA = timedelta(seconds=3000)
VCODE_TIMEOUT = 300
SESSION_TYPE = 'redis'
SESSION_REDIS = ''

VERIFYIDCODEURL = "http://aliyunverifyidcard.haoservice.com/idcard/VerifyIdcardv2"
VERIFYIDCODE_APPCODE = "422c011beb6f4b1b96a8de7c3330b464"

FBTIME_RANGE = 100

CKEDITOR_LANGUAGE = 'zh-cn'
CKEDITOR_PKG_TYPE = 'full'
CKEDITOR_FILE_UPLOADER = "/api/upload"
CKEDITOR_EXTRA_PLUGINS = ["font"]
