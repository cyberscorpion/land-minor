from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager



class User(AbstractBaseUser, PermissionsMixin):
    platformArray=(
        ('android',('android')),
        ('ios',('ios')),
    )
    account_address = models.CharField(max_length = 100)
    email = models.EmailField(_('email address'))
    username = models.CharField(_('username'),max_length = 50, unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default = True)
    objects = UserManager()
    max_bid = models.PositiveIntegerField(default = 300000)
    USERNAME_FIELD = 'username'
#    REQUIRED_FIELDS = ['email',]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
