from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from . import forms
from . import models

@method_decorator(login_required, name='dispatch')
class DetailCarView(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        car = self.get_object()

        comment_form = forms.CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()

        
        if 'buy_car' in request.POST:
            if car.quantity > 0:
                car.quantity -= 1
                car.save()
                models.Purchase_history.objects.create(user=request.user, car=car)
                messages.success(request, 'Car purchased successfully!')
            else:
                messages.warning(request, 'Out of Stock')

        return redirect('detail_car', id=car.id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context








