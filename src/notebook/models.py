from ckeditor.fields import RichTextField
from django.db import models

from kuila import settings


# Note model to store information about notes
class Note(models.Model):
    # ForeignKey to associate each note with a user; cascade delete if the user is deleted
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Field to store the title of the note
    title = models.CharField(max_length=255)

    # Field to store the content of the note using CKEditor for rich text
    content = RichTextField()

    # ForeignKey to associate each note with a category; optional field
    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE, blank=True, null=True)

    # Automatically set the creation date when a note is created
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically update the modification date when a note is updated
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Return the title of the note when converting the object to a string
        return self.title
