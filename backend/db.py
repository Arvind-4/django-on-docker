import os

from django.conf import settings

from backend.utils import is_true

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DJANGO_POSTGRES_DB = os.environ.get("POSTGRES_DB")
DJANGO_POSTGRES_USER = os.environ.get("POSTGRES_USER")
DJANGO_POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DJANGO_POSTGRES_HOST = os.environ.get("POSTGRES_HOST")
DJANGO_POSTGRES_PORT = os.environ.get("POSTGRES_PORT")
DJANGO_POSTGRES_IS_AVAILABLE = is_true(os.environ.get("POSTGRES_IS_AVAILABLE", False))

if all(
    [
        DJANGO_POSTGRES_DB,
        DJANGO_POSTGRES_USER,
        DJANGO_POSTGRES_PASSWORD,
        DJANGO_POSTGRES_HOST,
        DJANGO_POSTGRES_PORT,
    ]
):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DJANGO_POSTGRES_DB,
            "USER": DJANGO_POSTGRES_USER,
            "PASSWORD": DJANGO_POSTGRES_PASSWORD,
            "HOST": DJANGO_POSTGRES_HOST,
            "PORT": DJANGO_POSTGRES_PORT,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": settings.BASE_DIR / "db.sqlite3",
        }
    }
