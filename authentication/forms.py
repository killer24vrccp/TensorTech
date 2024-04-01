from django.utils.translation import gettext_lazy as _
from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'))
    password = forms.CharField(widget=forms.PasswordInput)



class RegisterForm(forms.Form):
    pass


