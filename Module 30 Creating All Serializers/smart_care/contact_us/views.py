from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.

class ContactusViewset(viewsets.ModelViewSet):
    queryset=models.ContactUs.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.ContactUsSerializer # JSON e object gulo convert korlam