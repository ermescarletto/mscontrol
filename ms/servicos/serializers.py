
from .models import *
from rest_framework import serializers


class CadastroItemChecklistSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        checklist = CadastroItemChecklist.objects.save(**validated_data)
        return checklist
    class Meta:
        model = CadastroItemChecklist



class CadastroChecklistSerializer(serializers.ModelSerializer):
    itens = serializers.StringRelatedField(many=True)
    tipo_servico = serializers.StringRelatedField(many=False)

    def create(self, validated_data):
        checklist = CadastroChecklist.objects.save(**validated_data)
        return checklist


    class Meta:
        model = CadastroChecklist
        fields = (
            'id',
            'descricao',
            'tipo_servico',
            'itens',
        )


class APIChecklistPreenchidoSerializer(serializers.ModelSerializer):
    ambiente = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    checklist = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    usuario = serializers.PrimaryKeyRelatedField(many=False, read_only=True)


    class Meta:
        model = ChecklistPreenchido
        fields = '__all__'
