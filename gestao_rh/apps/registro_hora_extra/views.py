#arquivo registro_hora_extra/views.py
from django.shortcuts import render

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View

from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra
from django.views.generic import (
    ListView,
    UpdateView,
    DeleteView,
    CreateView
)


# Create your views here.
class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(
            funcionario__empresa=empresa_logada)

class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    #fields = ['motivo', 'funcionario', 'horas']
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    # success_url = reverse_lazy('update_hora_extra_base')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs



class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')

class HoraExtraNovo(CreateView):
    model = RegistroHoraExtra
    #fields = ['motivo', 'funcionario', 'horas']
    #abaixo forma de se filtrar somente os funconários de uma empresa
    form_class = RegistroHoraExtraForm

    #este método é necessário para injetar o parâmetro user no método __init__ em
    #registro_hora_extra/forms.py
    def get_form_kwargs(self):
        kwargs = super(HoraExtraNovo, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
