
from .models import *
from rest_framework import serializers


class APIStatusAmbiente(serializers.ModelSerializer):
    ambiente = serializers.PrimaryKeyRelatedField(many=False, read_only=True)
    usuario = serializers.PrimaryKeyRelatedField(many=False, read_only=True)


    class Meta:
        model = StatusAmbiente
        fields = '__all__'
