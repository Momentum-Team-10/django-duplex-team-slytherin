from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Snippet(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=355)
    tag = models.CharField(max_length=355)
    language_field = models.CharField(max_length=355)
    created_at = models.DateTimeField(null=True, editable=False, blank=True, auto_now_add=True)
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="decks"
        )  
