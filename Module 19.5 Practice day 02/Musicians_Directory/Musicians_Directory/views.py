# from django.shortcuts import render
# from album.models import Album

# # Create your views here.
# def home(request):
#     data = Album.objects.all()
#     print(data)
   
#     return render(request, 'home.html', {'data': data})
from django.shortcuts import render,redirect
from album.models import Album
from musician.models import Musician
from album.forms import AlbumForm
from musician.forms import MusicianForm
from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class HomeClassView(generic.ListView):
    model = Album
    template_name = 'home.html'
    context_object_name = 'data'


@method_decorator(login_required, name= 'dispatch')
class EditPostView(generic.UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'edit.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')


@method_decorator(login_required, name= 'dispatch')
class MusicianClassView(generic.UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'edit.html'
    pk_url_kwarg ='id'
    success_url = reverse_lazy('home')



@method_decorator(login_required, name= 'dispatch')
class DeletePostView(generic.DeleteView):
    model = Album
    template_name = 'delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'
