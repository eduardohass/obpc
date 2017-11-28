from rest_framework import viewsets
from .models import Grupo, Pessoa, Regional, Endereco, Log
from .serializer import GrupoSerializer, PessoaSerializer, EnderecoSerializer, LogSerializer, RegionalSerializer

class GrupoViewSet(viewsets.ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer

class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class RegionalViewSet(viewsets.ModelViewSet):
    queryset = Regional.objects.all()
    serializer_class = RegionalSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer