from rest_framework import serializers
from gestao_rh.apps.funcionarios.models import Funcionario
from gestao_rh.apps.registro_hora_extra.api.serializers import RegistroHoraExtraSerializer


class FuncionarioSerializer(serializers.ModelSerializer):
    registrohoraextra_set = RegistroHoraExtraSerializer(many=True)
    class Meta:
        model = Funcionario
        fields = (
            'id', 'nome', 'departamentos', 'empresa', 'user',
            'total_horas_extra', 'registrohoraextra_set')
