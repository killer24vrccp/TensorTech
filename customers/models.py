from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django_tenants.models import TenantMixin, DomainMixin

from authentication.models import User

class Tenant(TenantMixin):
    """
    Class for creating client models using TenantMixin.
    """
    name = models.CharField(max_length=100)
    country = CountryField(verbose_name=_('Country'), null=True, blank=True)
    paid_until = models.DateField()
    is_active = models.BooleanField(default=True)
    on_trial = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    # default true. Schema will be automatically created and synced when it is saved
    auto_create_schema = True

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tenant'
        verbose_name = _('Tenant')
        verbose_name_plural = _('Tenants')


class Domain(DomainMixin):

    def __str__(self):
        return self.domain

    class Meta:
        db_table = 'domain'
        verbose_name = _('Domain')
        verbose_name_plural = _('Domains')


class Teams(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False)
    members = models.ManyToManyField(User, verbose_name=_('Members'), help_text=_('Add members to this team.'))
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.tenant.name

    class Meta:
        db_table = 'teams'
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
