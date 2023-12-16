from django.db import models
from brands.models import Brand
from django.contrib.auth.models import User
# Create your models here.
class Car(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    brand = models.ManyToManyField(Brand) 
    user_panel = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Set your default value here
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='cars/media/uploads/', blank = True, null = True)


    def __str__(self):
        return self.title 
    
class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comments by {self.name}"


class Purchase_history(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} buy this car name: {self.car.title}"
        
    