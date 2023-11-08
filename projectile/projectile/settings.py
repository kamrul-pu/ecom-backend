import os
import sys
from datetime import timedelta

from pathlib import Path

import dotenv

# Read environment variables
dotenv.read_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# The root of the git repo - Could be ~/project or ~/repo
REPO_DIR = os.path.realpath(os.path.join(BASE_DIR, ".."))
# The directory of the current user ie /home/django a.k.a. ~
HOME_DIR = os.path.realpath(os.path.join(REPO_DIR, ".."))
# The directory where collectstatic command copies/symlinks the files to
# This can/should be located at ~/staticfiles, preferrably outside the git repo
STATIC_DIR = os.path.realpath(os.path.join(HOME_DIR, "staticfiles"))
# The directory where different applications uploads media files to
# This can/should be located at ~/media, preferrably outside the git repo
MEDIA_DIR = os.path.realpath(os.path.join(HOME_DIR, "media"))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ENABLE_SILK = os.environ.get("ENABLE_SILK", False)

ALLOWED_HOSTS = []


# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
PROJECT_APPS = [
    "address",
    "core",
    "common",
    "order",
    "otp",
    "product",
    "search",
]
THIRD_PARTY_APPS = [
    "corsheaders",
    "django_filters",
    "django_elasticsearch_dsl",
    "django_cleanup.apps.CleanupConfig",
    "rest_framework",
    "rest_framework_simplejwt",
    "versatileimagefield",
]

if ENABLE_SILK:
    THIRD_PARTY_APPS += ["silk"]

if DEBUG:
    THIRD_PARTY_APPS += ["drf_spectacular"]

INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Enable Silk middleware if ENABLE SILK is True
if ENABLE_SILK:
    MIDDLEWARE += [
        "silk.middleware.SilkyMiddleware",
    ]

ROOT_URLCONF = "projectile.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "projectile.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Dhaka"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT = STATIC_DIR
STATIC_URL = "/static/"

MEDIA_ROOT = MEDIA_DIR
MEDIA_URL = "/media/"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

APPEND_SLASH = False

AUTH_USER_MODEL = "core.User"

# Versatile Image settings
VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    "cache_length": 2592000,
    # The name of the cache you'd like `django-versatileimagefield` to use.
    # Defaults to 'versatileimagefield_cache'. If no cache exists with the name
    # provided, the 'default' cache will be used instead.
    "cache_name": "versatileimagefield_cache",
    # The save quality of modified JPEG images. More info here:
    # https://pillow.readthedocs.io/en/latest/handbook/image-file-formats.html#jpeg
    # Defaults to 70
    "jpeg_resize_quality": 70,
    # The name of the top-level folder within storage classes to save all
    # sized images. Defaults to '__sized__'
    "sized_directory_name": "__sized__",
    # The name of the directory to save all filtered images within.
    # Defaults to '__filtered__':
    "filtered_directory_name": "__filtered__",
    # The name of the directory to save placeholder images within.
    # Defaults to '__placeholder__':
    "placeholder_directory_name": "__placeholder__",
    # Whether or not to create new images on-the-fly. Set this to `False` for
    # speedy performance but don't forget to 'pre-warm' to ensure they're
    # created and available at the appropriate URL.
    "create_images_on_demand": True,
    # A dot-notated python path string to a function that processes sized
    # image keys. Typically used to md5-ify the 'image key' portion of the
    # filename, giving each a uniform length.
    # `django-versatileimagefield` ships with two post processors:
    # 1. 'versatileimagefield.processors.md5' Returns a full length (32 char)
    #    md5 hash of `image_key`.
    # 2. 'versatileimagefield.processors.md5_16' Returns the first 16 chars
    #    of the 32 character md5 hash of `image_key`.
    # By default, image_keys are unprocessed. To write your own processor,
    # just define a function (that can be imported from your project's
    # python path) that takes a single argument, `image_key` and returns
    # a string.
    "image_key_post_processor": None,
    # Whether to create progressive JPEGs. Read more about progressive JPEGs
    # here: https://optimus.io/support/progressive-jpeg/
    "progressive_jpeg": False,
}


VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    "product_images": [
        ("full_size", "url"),
        ("small", "thumbnail__400x400"),
        ("medium", "thumbnail__600x600"),
        ("large", "thumbnail__1000x1000"),
    ],
}

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
        "rest_framework.renderers.BrowsableAPIRenderer",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_THROTTLE_RATES": {"anon": "300/minute", "user": "1200/minute"},
    # "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 40,
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=15),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
}

# Spectacular Documentation settings
SPECTACULAR_SETTINGS = {
    "TITLE": "Ecom Backend",
    "DESCRIPTION": "This is a single vendor ecommerce project",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

# Cors alowed origin
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]


TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN", "")
TWILIO_PHONE_NUMBER = os.environ.get("TWILIO_PHONE_NUMBER", "")

# Elastic Search
# ES_INDEX_SETTINGS = {
#     "number_of_shards": 1,
#     "number_of_replicas": 0,
# }

ELASTICSEARCH_DSL = {
    "default": {
        "hosts": "http://127.0.0.1:9200",
    },
}


# ES_PAGINATION_SIZE = 1000
# ES_MAX_PAGINATION_SIZE = 10000
# ES_CUSTOM_DOC_CHUNK_SIZE = 10000
# ES_DEFAULT_DOC_CHUNK_SIZE = 1000
# ELASTICSEARCH_DSL_PARALLEL = False
# ELASTICSEARCH_DSL_PARALLEL_CACHE_PREFIX = "elastic_search_record"


# Redis Caching
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379",
    }
}
