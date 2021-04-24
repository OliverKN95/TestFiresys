from rest_framework import routers, serializers, viewsets
from .models import test, person


class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'


class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields = '__all__'


class itunesSerializer(serializers.Serializer):
    """
    Serializer para traer información de Itunes
    """
    quantity = serializers.IntegerField(required=False)