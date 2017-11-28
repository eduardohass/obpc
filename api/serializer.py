from rest_framework import serializers
from .models import Grupo, Pessoa, Regional, Endereco, Log

class GrupoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:grupo-detail")

    class Meta:
        model = Grupo
        fields = "__all__"

class PessoaSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:pessoa-detail")

    class Meta:
        model = Pessoa
        fields = "__all__"


class EnderecoSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:endereco-detail")

    class Meta:
        model = Endereco
        fields = "__all__"


class RegionalSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:regional-detail")

    class Meta:
        model = Regional
        fields = "__all__"

class LogSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:log-detail")

    class Meta:
        model = Log
        fields = "__all__"
