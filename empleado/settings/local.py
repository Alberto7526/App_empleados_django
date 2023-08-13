from .base import *

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": 'db_empleado',
        "USER": 'albapp',
        "PASSWORD": 'albapp',
        "HOST": 'localhost',
        "PORT": '5432',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR.child('static')]

# se configura la ruta para guardar los archivos multimedia 
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.child('media')