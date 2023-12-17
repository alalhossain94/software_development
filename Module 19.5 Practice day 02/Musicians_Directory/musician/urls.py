# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.add_musician, name='add_musician'),
#     path('edit/<int:id>', views.edit_musician, name='edit_musician'),
# ]

# from django.urls import path
# from .views import AddMusicianClassView, EditMusicianClassView

# urlpatterns = [
#     path('add_musician/', AddMusicianClassView.as_view(), name='add_musician'),
#     path('edit_musician/<int:id>/', EditMusicianClassView.as_view(), name='edit_musician'),
# ]

from django.urls import path,include
from .views import  EditMusicianClassView
from . import views
urlpatterns = [
    path('add/',views.AddMusician.as_view(),name='add_musician'),
    path('edit_musician/<int:id>/', EditMusicianClassView.as_view(), name='edit_musician'),
    path('register/', views.SignUpViewClass.as_view(), name='register'),
    path('login/',views.UserLoginViewClass.as_view(), name = 'login'),
    path('logout/',views.UserLogoutViewClass.as_view(), name = 'logout'),
]