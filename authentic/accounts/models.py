from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .manager import UserManager


class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 223, unique=True)
    first_name = models.CharField(max_length = 223)
    last_name = models.CharField(max_length = 223)


    USERNAME_FIELD = "email"
    
    REQUIRED_FIELDS = ["first_name","last_name"]
    objects = UserManager()

    def __str__(self):
        return self.email
