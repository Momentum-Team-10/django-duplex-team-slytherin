from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

class User(AbstractUser):
    def __repr__(self):
        return f"<User username={self.username}>"
    
    def __str__(self):
        return self.username


class Snippet(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=355)
    tag = models.CharField(max_length=355)
    language_field = models.CharField(max_length=355)
    created_at = models.DateTimeField(null=True, editable=False, blank=True, auto_now_add=True)
    author = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            related_name="snippets"
        )  
    
    
    def __str__(self):
        return self.title

