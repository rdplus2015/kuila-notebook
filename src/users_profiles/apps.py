# users_profiles/apps.py

from django.apps import AppConfig


class UsersProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users_profiles'

    def ready(self):
        import users_profiles.signals  # noqa: F401
