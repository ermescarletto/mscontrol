from .models import *
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator





class CadastroItemChecklistSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        checklist = CadastroItemChecklist.objects.save(**validated_data)
        return checklist
    class Meta:
        model = CadastroItemChecklist


class ChecklistSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        checklist = Checklist.objects.save(**validated_data)
        return checklist
    class Meta:
        model = Checklist





class CadastroChecklistSerializer(serializers.ModelSerializer):
    itens = serializers.StringRelatedField(many=True)
    tipo_servico = serializers.StringRelatedField(many=False)



    def create(self, validated_data):
        checklist = CadastroChecklist.objects.save(**validated_data)
        return checklist


    class Meta:
        model = CadastroChecklist
        fields = (
            'descricao',
            'tipo_servico',
            'itens',
        )