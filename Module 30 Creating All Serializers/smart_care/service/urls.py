from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router=DefaultRouter() # amader Router

router.register('', views.ServiceViewset) # Router er Antena

urlpatterns = [
    path('', include(router.urls))
]