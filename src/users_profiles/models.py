from django.conf import settings
from django.db import models


class KuilaUserProfile(models.Model):
    # One-to-One relationship with the user model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    # Field for user's avatar image, allowing null and blank values
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    # Field for user's first name, allowing blank values
    first_name = models.CharField(max_length=30, blank=True)
    # Field for user's last name, allowing blank values
    last_name = models.CharField(max_length=30, blank=True)
    # Field for user's phone number, allowing blank values
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        # Return a string representation of the user's full name
        return f'{self.first_name} {self.last_name}'
