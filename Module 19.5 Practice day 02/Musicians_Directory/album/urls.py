from django.urls import path
from . import views
from .views import AddAlbumClassView,EditAlbumView,DeleteAlbumView

urlpatterns = [
    # path('', views.add_album, name='add_album'),
    path('add_album/', AddAlbumClassView.as_view(), name='add_album'),
    # path('edit/<int:id>', views.edit_album, name='edit_album'),
    path('album/edit/<int:id>/', EditAlbumView.as_view(), name='edit-album'),
    # path('delete/<int:id>', views.delete_album, name='delete_album'),
    path('album/delete/<int:id>/', DeleteAlbumView.as_view(), name='delete-album'),

]
