#arquivo funcionarios/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import Funcionario

# Create your views here.
"""  usada para teste
def home(request):
    return HttpResponse('Ola Funcionario')
"""

class FuncionariosList(ListView):
    model = Funcionario

    #overrider método de query do django para listar somente os
    #funcionarios da mesma empresa do usuario logado
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')

class FuncionarioNovo(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    #overhide método django
    def form_valid(self, form):
        funcionario = form.save(commit=False) #false para não atualizar bd por enquanto
        listaNomes = funcionario.nome.split(' ')
        username = listaNomes[0]
        if ( len(listaNomes) > 1):
            username += listaNomes[1]
        else:
            username += "User"
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)
