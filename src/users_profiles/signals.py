from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import KuilaUserProfile


# Signal receiver to create or update a user profile when a user is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Create a KuilaUserProfile instance for the newly created user
        KuilaUserProfile.objects.create(user=instance)
    # Update the user's profile (this is redundant with the second signal handler)
    instance.profile.save()


# Signal receiver to save the user profile when a user is saved
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def save_user_profile(sender, instance, **kwargs):
    # Save the user's profile (this assumes the profile is already created)
    instance.profile.save()
