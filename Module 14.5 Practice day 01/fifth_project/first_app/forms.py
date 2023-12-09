from django import forms
from django.forms.widgets import NumberInput
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class contactForm(forms.Form):
    name=forms.CharField(label="Enter your name ")
    email=forms.EmailField(label="User Email ")
    comment=forms.CharField(widget=forms.Textarea)
    age=forms.IntegerField()
    weight=forms.FloatField()
    balance=forms.DecimalField()
    check=forms.BooleanField()
    birthday=forms.CharField()
    appointment=forms.CharField(label="Appointment")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField()
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))