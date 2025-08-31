from django.db import models
from django.contrib.auth.models import  AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Product(models.Model):
   name = models.CharField(max_length=100, blank=True, null=True)
   buying_price = models.DecimalField(max_digits=10, decimal_places=2)
   selling_price = models.DecimalField(max_digits=10, decimal_places=2)
   description = models.TextField(blank=True)
   
   def __str__(self):
       return self.name

   def profit(self):
        return self.selling_price - self.buying_price
