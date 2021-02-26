from django.contrib import admin
from .models import Departamento

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'empresa',)
    list_filter = ('nome',)
    search_fields = ('nome',)


admin.site.register(Departamento,DepartamentoAdmin)
