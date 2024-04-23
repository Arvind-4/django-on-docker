import os

from backend.utils import is_true

SESSION_COOKIE_SECURE = is_true(os.environ.get("DJANGO_SESSION_COOKIE_SECURE"))
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
