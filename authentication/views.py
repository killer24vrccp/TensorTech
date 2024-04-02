from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View

from authentication.forms import LoginForm


# Create your views here.


class LoginView(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('webcore:index')
            else:
                # Return an 'invalid login' error message.
                return render(request, self.template_name, {'form': form, 'error_message': 'Invalid email or password.'})
        else:
            return render(request, self.template_name, {'form': form})
