from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers

# Create your views here.
class AppointmentViewset(viewsets.ModelViewSet):
    queryset=models.Appointment.objects.all() # ContactUs model theke shob object nilam
    serializer_class=serializers.AppointmentSerializer # JSON e object gulo convert korlam

# Custom Query Set
    
    def get_queryset(self):
        queryset= super().get_queryset() # parent ba 7 line k inherite korlam
        patient_id=self.request.query_params.get('patient_id')
        if patient_id:
            queryset=queryset.filter(patient_id=patient_id)
        return queryset