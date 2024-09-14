from django.db import models

# Importing settings to reference the custom user model (AUTH_USER_MODEL)
from kuila import settings


# Defining the Category model
class Category(models.Model):
    # Field to store the category name with a max length of 200 characters
    name = models.CharField(max_length=200)

    # ForeignKey to associate each category with a user
    # If the user is deleted, all associated categories are also deleted (CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # String representation of the Category model, which returns the category name
    def __str__(self):
        return self.name
