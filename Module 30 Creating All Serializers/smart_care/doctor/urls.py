from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router=DefaultRouter() # amader Router

router.register('list', views.DoctorViewset) # Router er Antena
router.register('specialization', views.SpecializationViewset) # Router er Antena
router.register('designation', views.DesignationViewset) # Router er Antena
router.register('available_time', views.AvailableTimeViewset) # Router er Antena
router.register('reviews', views.ReviewViewset) # Router er Antena

urlpatterns = [
    path('', include(router.urls))
]