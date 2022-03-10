from django.contrib import admin
from .models import Snippet, User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Snippet)
admin.site.register(User, UserAdmin)  