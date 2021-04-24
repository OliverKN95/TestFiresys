from django.shortcuts import render
from django.db import models
from rest_framework import viewsets
from .models import test
from .serializers import testSerializer

# Create your views here.


class testViewset(viewsets.ModelViewSet):
    queryset = test.objects.all()
    serializer_class = testSerializer
