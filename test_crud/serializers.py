from rest_framework import routers, serializers, viewsets
from .models import test

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = '__all__'