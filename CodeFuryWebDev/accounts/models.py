from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(_('user name'), unique=True, max_length=25)
    f_name = models.CharField(_('fist name'), max_length=25)
    l_name = models.CharField(_('last name'), max_length=25)
    g_choices = (('male', 'Male'),
                 ('female', 'Female'),
                 ('other', 'Other'))
    gender = models.CharField(_('gender'), max_length=6, choices=g_choices)
    dob = models.DateField(_('date of birth'), default='2022-08-13')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'gender', 'dob']

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class StartUps:
    username = models.CharField(_('user name'), unique=True, max_length=25)
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=25)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name']

    objects = CustomUserManager()

    def __str__(self):
        return self.username
