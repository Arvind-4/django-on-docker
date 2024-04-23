import os
from django.conf import settings

from backend.utils import is_true, split_with_comma

CSRF_COOKIE_SECURE = is_true(os.environ.get("DJANGO_CSRF_COOKIE_SECURE"))
CSRF_TRUSTED_ORIGINS = split_with_comma(
    os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", settings.ALLOWED_HOSTS)
)
