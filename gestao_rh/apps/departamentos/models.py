#arquivo departamentos/models.py
from django.db import models
from django.urls import reverse
from gestao_rh.apps.empresas.models import Empresa

# Create your models here.
class Departamento(models.Model):
    objects = None
    nome = models.CharField(max_length=70)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_departamentos')
