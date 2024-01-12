from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class PatientViewset(viewsets.ModelViewSet):
    queryset=models.Patient.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.PatientSerializer # JSON e object gulo convert korlam