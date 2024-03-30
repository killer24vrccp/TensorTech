from django.contrib import admin

# Register your models here.


from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from customers.models import Tenant


@admin.register(Tenant)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'paid_until')

