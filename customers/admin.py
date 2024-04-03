from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from customers.models import Tenant, Domain


@admin.register(Tenant)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('schema_name', 'name', 'country', 'is_active', 'paid_until', 'on_trial')


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['domain', 'tenant']
