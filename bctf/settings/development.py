from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z6u+3oksy50%8xepzcrgc&1t3mgjd6)oy=qyqm-hb5-j*3a=q@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*", ]

if DEBUG == True:
    INSTALLED_APPS += ['django.contrib.admin', ]


# Development settings
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")