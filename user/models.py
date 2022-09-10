from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class Profile(AbstractUser):

    email = models.EmailField(_("email address"), blank=True, unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]





