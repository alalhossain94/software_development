from django.shortcuts import render
from Task.models import TaskModel

# Create your views here.

def home(request):
    return render(request, 'home.html')

def show_task(request):
    data = TaskModel.objects.all()

    return render(request, 'show_tasks.html', {'data': data})

