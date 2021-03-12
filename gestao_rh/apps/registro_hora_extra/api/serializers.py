from rest_framework import serializers
from gestao_rh.apps.registro_hora_extra.models import RegistroHoraExtra


class RegistroHoraExtraSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroHoraExtra
        fields = ('motivo', 'funcionario', 'horas', 'utilizada')
