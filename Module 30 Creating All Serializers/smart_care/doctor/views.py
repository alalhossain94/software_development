from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class DoctorViewset(viewsets.ModelViewSet):
    queryset=models.Doctor.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.DoctorSerializer # JSON e object gulo convert korlam

class SpecializationViewset(viewsets.ModelViewSet):
    queryset=models.Specialization.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.SpecializtionSerializer # JSON e object gulo convert korlam

class DesignationViewset(viewsets.ModelViewSet):
    queryset=models.Designation.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.DesignationSerializer # JSON e object gulo convert korlam

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset=models.AvailableTime.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.AvailableTimeSerializer # JSON e object gulo convert korlam

class ReviewViewset(viewsets.ModelViewSet):
    queryset=models.Review.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.ReviewSerializer # JSON e object gulo convert korlam