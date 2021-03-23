#arquivo funcionarios/views.py

#geração relatórios
import io


from reportlab.pdfgen import canvas
from django.http import FileResponse
import xhtml2pdf.pisa as pisa
from django.template.loader import get_template
from django.views.generic.base import View, TemplateView
from django.utils.translation import gettext as _    #para gettext

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
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['report_button'] = _("Employee report")  #o _ é do import acima as _
        return context

    #overrider método de query do django para listar somente os
    #funcionarios da mesma empresa do usuario logado
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)

class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos','de_ferias']

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
        funcionario.de_ferias = False
        funcionario.save()
        return super(FuncionarioNovo, self).form_valid(form)

def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    #cmd abaixo - fazer o download quando clicar no link
    response['Content-Disposition'] = 'attachment; filename="RelatFuncHoraExtra.pdf"'

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 810, 'Relatorio de funcionarios')

    funcionarios = Funcionario.objects.filter(
        empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s - Total Hora Extra: %.2f'

    p.drawString(0, 800, '_' * 150)

    y = 750
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (
            funcionario.nome, funcionario.total_horas_extra))
        y -= 20
        for a1 in funcionario.get_lista_horas_extra():
            str2 = a1.motivo + ' - Horas: ' + str(a1.horas) + '- Utilizada: ' + a1.get_hora_utilizada()
            p.drawString(50, y, str2)
            y -= 20

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

class Render:
    @staticmethod
    def render(path: str, params: dict, filename: str):
        template = get_template(path)
        html = template.render(params)
        response = io.BytesIO()
        pdf = pisa.pisaDocument(
            io.BytesIO(html.encode("UTF-8")), response)
        if not pdf.err:
            response = HttpResponse(
                response.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment;filename=%s.pdf' % filename
            return response
        else:
            return HttpResponse("Error Rendering PDF", status=400)
"""
class Pdf(View):
    def get(self, request):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')
"""

class Pdf(View):
    def get(self, request):
        funcionarios = Funcionario.objects.filter(
            empresa=request.user.funcionario.empresa)
        params = {
            'funcionarios' : funcionarios,
            'request': request,
        }
        return Render.render('funcionarios/relatorio.html', params, 'myfile')

class PdfDebug(TemplateView):
    template_name = 'funcionarios/relatorio.html'