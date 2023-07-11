from django import forms
from django.forms import ModelForm

from .models import URL


class UrlForm(ModelForm):
    class Meta:
        model = URL
        fields = ['linked_url', 'shortened_code', 'is_password_protected', 'can_expire', 'password', 'expiration_time']
        widgets = {
            'password': forms.PasswordInput(),
            'expiration_time': forms.DateTimeInput(attrs={'placeholder': 'YYYY-MM-DD HH:MM'}),
        }
