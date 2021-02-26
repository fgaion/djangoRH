from django.forms import ModelForm
from .models import RegistroHoraExtra
#abaixo não pode colocar o ponto antes de gestao_rh
from gestao_rh.apps.funcionarios.models import Funcionario

#sobrepor método init paraf filtrar somente os funcionários de uma empresa
class RegistroHoraExtraForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(RegistroHoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['funcionario'].queryset = Funcionario.objects.filter(
            empresa=user.funcionario.empresa)

    class Meta:
        model = RegistroHoraExtra
        fields = ['motivo', 'funcionario', 'horas']

