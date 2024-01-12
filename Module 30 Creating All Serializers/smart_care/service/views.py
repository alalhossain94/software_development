from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class ServiceViewset(viewsets.ModelViewSet):
    queryset=models.Service.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.ServiceSerializer # JSON e object gulo convert korlam