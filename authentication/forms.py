from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from authentication.models import User
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'))
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fieldsets = [
            (_('Personal info'), {
                'fields': [
                    'email', 'password',
                ],
            }),
        ]

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise ValidationError(_("Les mots de passe ne correspondent pas "))

        # Always return the full collection of cleaned data
        return cleaned_data

