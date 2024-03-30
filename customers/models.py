from django.db import models
from authentication.models import User
from django_tenants.models import TenantMixin, DomainMixin


class Tenant(TenantMixin):
    """
    Class for creating client models using TenantMixin.
    """
    name = models.CharField(max_length=100)
    contact = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    # default true. Schema will be automatically created and synced when it is saved
    auto_create_schema = True


class Domain(DomainMixin):
    pass
