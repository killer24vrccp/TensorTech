# Delos/auth/models.py
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission, Group
from django.utils.translation import gettext_lazy as _
from authenticationBase.authenticationShared.manager.managers import CustomUserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        verbose_name=_('Email'),
        max_length=255,
        blank=False
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name=_('First Name'),
        blank=True
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_('Last Name'),
        blank=True
    )

    phone_number = models.CharField(max_length=10, verbose_name=_('Phone Number'), blank=True)
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    # override groups and user_permissions fields
    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions', blank=True)

    USERNAME_FIELD = 'email'
    objects = CustomUserManager()
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'user'
        verbose_name = _("user")
        verbose_name_plural = _("users")

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True