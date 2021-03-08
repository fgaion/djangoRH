#arquivo registro_hora_extra/models.py
from django.db import models
from django.urls import reverse
from gestao_rh.apps.funcionarios.models import Funcionario

# Create your models here.
class RegistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)
    utilizada = models.BooleanField(default=False)

    def __str__(self):
        return self.motivo

    def get_hora_utilizada(self):
        if ( self.utilizada):
            return("Sim")
        else:
            return("Não")

    def get_absolute_url(self):
        return reverse('update_funcionario', args=[self.funcionario.id])
        #return reverse('update_hora_extra', args=[self.id])
