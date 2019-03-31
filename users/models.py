from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER')
    )
    db_table = 'user'

    email = models.EmailField(_('email address'), max_length=225, unique=True, blank=False)
    username = models.CharField(_('username'), max_length=225, unique=True, blank=False)
    gender = models.CharField(_('gender'), max_length=5, blank=False)
    first_name = models.CharField(_('first name'), max_length=225, null=True)
    last_name = models.CharField(_('last name'), max_length=225, null=True)
    mobile = models.CharField(_('mobile'), max_length=225, null=True)
    created_at = models.DateTimeField(_('date created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('dated updated'), auto_now=True)
    is_active = models.BooleanField(_('active'), default=False)
    is_staff = models.BooleanField(_('staff'), default=False)
    avatar = models.CharField(max_length=225, null=True, blank=True)
    last_seen = models.DateTimeField(_('last seen'), null=True)

    objects = UserManager()
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    class Meta:
        db_table = 'users'
        verbose_name = _('user')
        verbose_name_plural = _('users')

