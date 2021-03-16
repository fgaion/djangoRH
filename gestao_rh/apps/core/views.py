#arquivo core/views.py
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from gestao_rh.apps.funcionarios.models import Funcionario

#Django REST
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from gestao_rh.apps.core.serializers import UserSerializer, GroupSerializer

from .tasks import send_relatorio

# Create your views here.
@login_required
def home(request):
    data = {}
    data['usuario'] = request.user

    return render(request, 'core/index.html',data)

def celery(request):
    send_relatorio.delay()
    #send_relatorio()
    return HttpResponse('Tarefa incluida na fila para execucao')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)