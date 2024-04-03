from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from authentication.forms import LoginForm
from customers.models import Domain


class LoginView(View):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)

                # Check if the user is associated with a team
                if user.team is None:
                    messages.add_message(request, messages.ERROR, "You do not belong to any team.")
                    return render(request, self.template_name, {'form': form})

                team = user.team

                # Check if the team has a tenant associated with it
                if team.tenant is None:
                    messages.add_message(request, messages.ERROR, "Your team doesn't have a tenant associated.")
                    return render(request, self.template_name, {'form': form})

                tenant = team.tenant

                try:
                    domain = Domain.objects.get(tenant=tenant)
                    tenant_domain = domain.domain
                except ObjectDoesNotExist:
                    messages.add_message(request, messages.ERROR, "No Domain associated with your Tenant.")
                    return render(request, self.template_name, {'form': form})

                # Build the redirection URL
                domain_url = request.scheme + '://' + tenant_domain

                # Redirection vers le domaine du locataire
                return redirect(domain_url)
            else:
                # Retourner un message d'erreur de connexion invalide
                return render(request, self.template_name,
                              {'form': form, 'error_message': 'Invalid email or password.'})
        else:
            return render(request, self.template_name, {'form': form})