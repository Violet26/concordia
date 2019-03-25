import os

from .settings_template import *  # NOQA ignore=F405
from .settings_template import DATABASES, INSTALLED_APPS, LOGGING, MIDDLEWARE

LOGGING["handlers"]["stream"]["level"] = "DEBUG"
LOGGING["handlers"]["file"]["level"] = "DEBUG"
LOGGING["handlers"]["file"]["filename"] = "./logs/concordia-web.log"
LOGGING["handlers"]["celery"]["level"] = "DEBUG"
LOGGING["handlers"]["celery"]["filename"] = "./logs/concordia-celery.log"
LOGGING["loggers"]["django"]["level"] = "DEBUG"
LOGGING["loggers"]["celery"]["level"] = "DEBUG"

DEBUG = True

DATABASES["default"]["PORT"] = "54323"

ALLOWED_HOSTS = ["127.0.0.1", "0.0.0.0", "*"]

CELERY_BROKER_URL = "redis://localhost:63791/0"
CELERY_RESULT_BACKEND = CELERY_BROKER_URL

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_FILE_PATH = "/tmp/concordia-messages"  # change this to a proper location
DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL", "")
DEFAULT_TO_EMAIL = DEFAULT_FROM_EMAIL

ELASTICSEARCH_DSL_AUTOSYNC = False

ELASTICSEARCH_DSL_SIGNAL_PROCESSOR = (
    "django_elasticsearch_dsl.signals.RealTimeSignalProcessor"
)
ELASTICSEARCH_DSL = {"default": {"hosts": "localhost:9200"}}

INSTALLED_APPS += ["django_elasticsearch_dsl"]

REGISTRATION_SALT = "django_registration"  # doesn't need to be secret

INSTALLED_APPS += ["debug_toolbar"]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]
INTERNAL_IPS = ("127.0.0.1",)

INSTALLED_APPS += ("django_extensions",)
SHELL_PLUS_PRE_IMPORTS = [
    ("concordia.utils", "get_anonymous_user"),
    ("concordia.models", "TranscriptionStatus"),
]

S3_BUCKET_NAME = "crowd-dev-content"
EXPORT_S3_BUCKET_NAME = "crowd-dev-export"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_STORAGE_BUCKET_NAME = S3_BUCKET_NAME
AWS_DEFAULT_ACL = None  # Don't set an ACL on the files, inherit the bucket ACLs
MEDIA_URL = "https://%s.s3.amazonaws.com/" % S3_BUCKET_NAME

# Celery 4.2.1 needs this when using docker DB
# see https://github.com/celery/celery/issues/4878
# For some reason, in AWS it doesn't seem to be an issue
DATABASES["default"]["CONN_MAX_AGE"] = 0
