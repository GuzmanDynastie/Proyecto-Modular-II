from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class administrador(models.Model):
    Name = models.CharField(_("Name"), max_length=50)
    Surname = models.CharField(_("Surname"), max_length=50)
    Email = models.EmailField(_("Email"), max_length=254)
    Password = models.CharField(_("Password"), max_length=50)
    Cellular = models.CharField(_("Cellular"), max_length=10)
    
    class Meta:
        db_table = 'administrador'