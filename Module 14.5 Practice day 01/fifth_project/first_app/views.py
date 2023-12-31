from django.shortcuts import render
from .forms import contactForm

def home(request):
    return render(request, './first_app/home.html')

def about(request):
    if request.method=="POST":
        # print(request.POST)
        name=request.POST.get('username')
        email=request.POST.get('email')
        select=request.POST.get('select')
        return render(request, './first_app/about.html', {'name': name, 'email': email, 'select':select})
    else:
        return render(request, './first_app/about.html')

def submit_form(request):
    return render(request, './first_app/form.html')

def DjangoForm(request):
    form=contactForm(request.POST)
    # print(request.POST)
    if form. is_valid():
        print(form.cleaned_data)

    return render(request, './first_app/django_form.html', {'form': form})



