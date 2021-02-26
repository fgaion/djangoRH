from django.contrib import admin
from .models import Funcionario

# Register your models here.
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'user', 'empresa',)
    list_filter = ('nome',)
    search_fields = ('nome',)


admin.site.register(Funcionario,FuncionarioAdmin)