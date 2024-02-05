from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email 
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def email_validator(self,email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("please enter a email address"))
    """
    Custom user model manager where email is the unique identifier
    for authentication instead ofernames.
    """

    def create_user(self, email,password,first_name,last_name, **extra_fields):
        if not email:
            raise ValueError(_('Users must have an email address'))
        else:
            email = self.normalize_email(email)
            self.email_validator(email)
        if not first_name:
            raise ValueError(_('Users must have an first name'))
        if not last_name:
            raise ValueError(_('Users must have an last name'))
        
        user = self.model(email=email,first_name = first_name,last_name = last_name,**extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email,password,first_name,last_name, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        user = self.create_user(
            email,first_name,last_name,password,**extra_fields)
        user.save(using = self._db)
        return user
