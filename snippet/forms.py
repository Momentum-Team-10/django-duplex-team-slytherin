from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'title',
            'description',
            'tag',
            'language_field',
        ]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = [
            'first_name',
            'last_name',
            'email',
            'employer',
        ]        