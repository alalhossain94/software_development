from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meal/', views.meal_list, name='meal_list'),
    
]
