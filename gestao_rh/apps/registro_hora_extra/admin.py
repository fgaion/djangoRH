#arquivo registro_hora_extra/admin.py
from django.contrib import admin
from .models import RegistroHoraExtra, Funcionario

# Register your models here.
class RegistroHoraExtraAdmin(admin.ModelAdmin):
    list_display = ('motivo','funcionario', 'horas','utilizada')
    list_filter = ('motivo','funcionario__nome','utilizada')
    search_fields = ('motivo',)


admin.site.register(RegistroHoraExtra,RegistroHoraExtraAdmin)