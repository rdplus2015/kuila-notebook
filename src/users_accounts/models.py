from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Custom manager for KuilaUser
class KuilaUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        # Ensure the email is provided
        if not email:
            raise ValueError('The Email field must be set')

        # Normalize the email address
        email = self.normalize_email(email)

        # Create a new user instance with the provided email and additional fields
        user = self.model(email=email, **extra_fields)

        # Set the user's password
        user.set_password(password)

        # Save the user to the database
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        # Set default values for superuser privileges
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        # Create and return a superuser with the provided email and password
        return self.create_user(email, password, **extra_fields)


# Custom user model
class KuilaUser(AbstractBaseUser, PermissionsMixin):
    # Remove the default username field
    username = None

    # Define the email field, which will be used as the unique identifier
    email = models.EmailField(unique=True, blank=False, max_length=255)

    # Timestamp for user creation
    created_at = models.DateTimeField(auto_now_add=True)

    # Boolean fields for user permissions and status
    is_staff = models.BooleanField(default=False)  # Indicates if the user is staff
    is_active = models.BooleanField(default=True)  # Indicates if the user is active
    is_superuser = models.BooleanField(default=False)  # Indicates if the user is a superuser

    # Use the custom user manager
    objects = KuilaUserManager()

    # Define the unique identifier for the user
    USERNAME_FIELD = 'email'

    # Fields required when creating a user (none in this case)
    REQUIRED_FIELDS = []

    def __str__(self):
        # Return the email as the string representation of the user
        return self.email
