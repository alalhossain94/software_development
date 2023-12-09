from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.

def add_album(request):
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    else:
        album_form = forms.AlbumForm()
    return render(request, 'add_album.html', {'form':album_form})


#  edit table record
def edit_album(request, id):
    data = models.Album.objects.get(pk=id)
    album_form = forms.AlbumForm(instance=data)
    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=data)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request, 'add_album.html', {'form':album_form})


# delete table record

def delete_album(request, id):
    record = models.Album.objects.get(pk=id)
    record.delete()
    return redirect('home')