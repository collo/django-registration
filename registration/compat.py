from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import django

__all__ = ['User', 'AUTH_USER_MODEL']

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Django 1.5+ compatibility
# https://github.com/toastdriven/django-tastypie/blob/d24b390f426b5da5121717913a446cc8b057ae20/tastypie/compat.py
if django.VERSION >= (1, 5):
    try:
        from django.contrib.auth import get_user_model
        User = get_user_model()
        username_field = User.USERNAME_FIELD
    except ImproperlyConfigured:
        # The the users model might not be read yet.
        # This can happen is when setting up the create_api_key signal, in your
        # custom user module.
        User = None
else:
    from django.contrib.auth.models import User
    username_field = 'username'
