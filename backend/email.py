import os

from backend.utils import is_true

EMAIL_HOST = os.environ.get("DJANGO_EMAIL_HOST", "localhost")
EMAIL_PORT = int(os.environ.get("DJANGO_EMAIL_PORT", 25))
EMAIL_HOST_USER = os.environ.get("DJANGO_EMAIL_HOST_USER", "replace@mail.com")
EMAIL_HOST_PASSWORD = os.environ.get("DJANGO_EMAIL_HOST_PASSWORD", "replace_password")
EMAIL_USE_TLS = is_true(os.environ.get("DJANGO_EMAIL_USE_TLS", "false"))

SERVER_EMAIL = os.environ.get("DJANGO_SERVER_EMAIL", "root@localhost")

DEFAULT_FROM_EMAIL = os.environ.get("DJANGO_DEFAULT_FROM_EMAIL", "sample@localhost")

ADMIN_NAME = os.environ.get("DJANGO_ADMIN_NAME", "Admin")
ADMIN_EMAIL = os.environ.get("DJANGO_ADMIN_EMAIL", "admin@localhost.com")
if ADMIN_EMAIL:
    ADMINS = [(ADMIN_NAME, ADMIN_EMAIL)]
