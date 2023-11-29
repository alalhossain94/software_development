from django.urls import path
# from first_app.views import home
from . import views
urlpatterns = [
    path("", views.home),
]
