from django.db import models
from django.contrib.auth.models import  AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
   username = None
   name = models.CharField(max_length=200)
   email = models.EmailField(unique=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []

   def __str__(self):
       return self.email
