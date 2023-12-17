# from django.shortcuts import render, redirect
# from . import forms
# from . import models
# # Create your views here.

# def add_musician(request):
#     if request.method == 'POST':
#         musician_form = forms.MusicianForm(request.POST)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('add_musician')
#     else:
#         musician_form = forms.MusicianForm()
#     return render(request, 'add_musician.html', {'form':musician_form})


# # edit musician
# def edit_musician(request, id):
#     data = models.Musician.objects.get(pk=id)
#     musician_form = forms.MusicianForm(instance=data)
#     if request.method == 'POST':
#         musician_form = forms.MusicianForm(request.POST, instance=data)
#         if musician_form.is_valid():
#             musician_form.save()
#             return redirect('home')

#     return render(request, 'add_musician.html', {'form':musician_form})


# from django.shortcuts import render, redirect
# from django.views import View
# from django.views.generic.edit import CreateView, UpdateView
# from django.urls import reverse_lazy
# from . import models, forms


from django.shortcuts import render,redirect
from . import forms
from django.views.generic.edit import CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from . import models


# @method_decorator(login_required, name= 'dispatch')
# class AddMusicianClassView(CreateView):
#     model = models.Musician
#     form_class = forms.MusicianForm
#     template_name = 'add_musician.html'
#     success_url = reverse_lazy('add_musician')



@method_decorator(login_required, name= 'dispatch')
class AddMusician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('add_musician')

    def form_valid(self, form):
        form.instance.musician = self.request.user
        return super().form_valid(form)

class EditMusicianClassView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.model.objects.get(pk=self.kwargs['id'])

def add_musician(request):
    return AddMusician.as_view()(request)

def edit_musician(request, id):
    return EditMusicianClassView.as_view()(request, id=id)
 



class SignUpViewClass(CreateView):
     template_name = 'form.html'
     success_url = reverse_lazy('register')
     form_class = forms.RegistationForm
     success_message = "Your account was created successfully "

     def form_valid(self,form):
          response = super().form_valid(form)
          messages.success(self.request, self.success_message)
          return response
     def get_context_data(self,**kwargs):
         context = super().get_context_data(**kwargs)
         context['type'] = 'Register'
         return context



class UserLoginViewClass(LoginView):
    template_name = 'form.html'
    
    def get_success_url(self):
        return reverse_lazy('homepage')
    
    def form_valid(self, form):
        messages.success(self.request, 'You are successfully logged in')
        # form
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Your provided information is incorrect')
        # form
        return super().form_invalid(form)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

@method_decorator(login_required, name= 'dispatch')
class UserLogoutViewClass(LogoutView):
    template_name = 'logout.html'
    def get_success_url(self):
       return reverse_lazy('homepage')
    
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)

        messages.success(self.request, "You have been successfully logged out.")
        return response