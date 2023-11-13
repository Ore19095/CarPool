from django.db import models

# Create your models here.
# creeate a user model with the fields used in register.html document 

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=8)
    is_passenger = models.BooleanField(default=True)
    asientos_disponibles = models.IntegerField(default=0)
    car_type = models.CharField(max_length=50, default='None')
    car_branch = models.CharField(max_length=50, default='None')
    
    # create a string representation of the user model
    def __str__(self):
        return self.username + " " + self.password + " " + self.email\
              + " " + self.phone 