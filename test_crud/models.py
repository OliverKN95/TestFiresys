from django.db import models
from django.utils.translation import ugettext_lazy as _
from datetime import datetime

# Create your models here.


class test(models.Model):
    name = models.CharField(max_length=100)


class person(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=_("Nombre"))
    last_name = models.CharField(max_length=100, verbose_name=_("Apellidos"))
    address = models.CharField(max_length=100, verbose_name=_("Dirección"))
    country = models.CharField(max_length=100, verbose_name=_("País"))
    zip = models.IntegerField(verbose_name=_("Código Postal"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))