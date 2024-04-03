from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django_tenants.utils import get_tenant_model, get_tenant_domain_model

from authentication.forms import LoginForm


# Create your views here.


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

                # Récupérer l'équipe associée à l'utilisateur
                if hasattr(user, 'team'):
                    team = user.team
                else:
                    # Ajouter ici la gestion de l'erreur s'il n'y a pas d'équipe associée à l'utilisateur
                    pass

                # Récupérer le locataire associé à l'équipe
                if hasattr(team, 'tenant'):
                    tenant = team.tenant
                else:
                    # Ajouter ici la gestion de l'erreur s'il n'y a pas de locataire associé à l'équipe
                    pass

                # Définir le locataire actif
                set_tenant(tenant)

                # Récupérer le domaine associé à ce locataire
                Domain = get_tenant_model().domain_set.get(tenant=tenant)
                domain_url = Domain.domain

                # Redirection vers le domaine du locataire
                return redirect(domain_url)
            else:
                # Retourner un message d'erreur de connexion invalide
                return render(request, self.template_name,
                              {'form': form, 'error_message': 'Invalid email or password.'})
        else:
            return render(request, self.template_name, {'form': form})