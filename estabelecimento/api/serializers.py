from rest_framework import serializers
from estabelecimento import models


class EstabelecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Estabelecimento
        fields = '__all__'


class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Atividade
        fields = '__all__'


class ObjetoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Objeto
        fields = '__all__'        


class DistritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Distrito
        fields = '__all__'   


class CidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cidade
        fields = '__all__'   


class EquipamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Equipamento
        fields = '__all__'   