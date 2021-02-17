#arquivo empresas/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from .models import Empresa

# Create your views here.
class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome']

    def form_valid(self, form):
        obj = form.save()  #passa a ter o obj empresa dispnível
        funcionario = self.request.user.funcionario
        funcionario.empresa = obj
        funcionario.save()
        return HttpResponse('Ok')

class EmpresaEdit(UpdateView):
    model = Empresa
    fields = ['nome']