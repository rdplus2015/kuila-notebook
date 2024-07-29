
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, Group, Permission
from django.db import models


# Custom manager for KuilaUser
class KuilaUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Ensure the email is provided
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)  # Normalize the email
        user = self.model(email=email, **extra_fields)  # Create a new user instance
        user.set_password(password)  # Set the password
        user.save(using=self._db)  # Save the user to the database
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Set default values for superuser privileges
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)  # Create a superuser


# Custom user model
class KuilaUser(AbstractBaseUser, PermissionsMixin):
    username = None  # Remove the username field
    email = models.EmailField(unique=True, blank=False, max_length=255)  # Email field
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for user creation
    is_staff = models.BooleanField(default=False)  # Indicates if the user is staff
    is_active = models.BooleanField(default=True)  # Indicates if the user is active
    is_superuser = models.BooleanField(default=False)  # Indicates if the user is a superuser

    objects = KuilaUserManager()  # Use the custom user manager
    USERNAME_FIELD = 'email'  # The unique identifier for the user
    REQUIRED_FIELDS = []  # Fields required when creating a user (none in this case)

    def __str__(self):
        return self.email  # Return the email as the string representation of the user
