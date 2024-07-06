# users_profiles/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import KuilaUserProfile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        KuilaUserProfile.objects.create(user=instance)
    instance.profile.save()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
