
# # Create your views here.
# def add_album(request):
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('add_album')
#     else:
#         album_form = forms.AlbumForm()
#     return render(request, 'add_album.html', {'form':album_form})

from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from . import forms ,models
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView,DeleteView
# Class based CrateView 
class AddAlbumClassView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('add_album')

    def form_valid(self, form):
        form.instance.album = self.request.user
        return super().form_valid(form)
    

#  edit table record
# def edit_album(request, id):
#     data = models.Album.objects.get(pk=id)
#     album_form = forms.AlbumForm(instance=data)
#     if request.method == 'POST':
#         album_form = forms.AlbumForm(request.POST, instance=data)
#         if album_form.is_valid():
#             album_form.save()
#             return redirect('home')
#     return render(request, 'add_album.html', {'form':album_form})

class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['id'])

    def form_valid(self, form):
        response = super().form_valid(form)
        return response

def edit_album(request, id):
    return EditAlbumView.as_view()(request, id=id)


# delete table record

# def delete_album(request, id):
#     record = models.Album.objects.get(pk=id)
#     record.delete()
#     return redirect('home')


class DeleteAlbumView(DeleteView):
    model = models.Album
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=self.kwargs['id'])

def delete_album(request, id):
    return DeleteAlbumView.as_view()(request, id=id)