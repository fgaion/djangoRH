#arquivo funcionarios/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from gestao_rh.apps.departamentos.models import Departamento
from gestao_rh.apps.empresas.models import Empresa
from django.db.models import Sum

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def get_lista_horas_extra(self):
        lista_horas = self.registrohoraextra_set.all()
        return lista_horas

    @property
    def total_horas_extra(self):
        #aggregate retorna uma lista com 2 elm [ 'horas__sum' : Decimal(<valor da soma>) ]
        total = 0
        #total = self.registrohoraextra_set.aggregate(Sum('horas'))['horas__sum']
        total = self.registrohoraextra_set.filter(
            utilizada=False).aggregate(
            Sum('horas'))['horas__sum']
        return total or 0

