from rest_framework import viewsets
from estabelecimento.api import serializers
from estabelecimento import models


class EstabelecimentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EstabelecimentoSerializer
    queryset = models.Estabelecimento.objects.all()


class AtividadeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AtividadeSerializer
    queryset = models.Atividade.objects.all()


class ObjetoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ObjetoSerializer
    queryset = models.Objeto.objects.all()


class DistritoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DistritoSerializer
    queryset = models.Distrito.objects.all()


class CidadeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CidadeSerializer
    queryset = models.Cidade.objects.all()


class EquipamentoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EquipamentoSerializer
    queryset = models.Equipamento.objects.all()

