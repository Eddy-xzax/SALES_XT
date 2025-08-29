from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import CustomUserSerializer
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

#class SignUpView(CreateView):
#   form_class = CustomUserCreationForm
#  success_url = reverse_lazy("login")
# template_name = "registration/registration.html"
#hope this works cause  if it doest am cooked

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def login(request):
    return render(request, "login.html")

def signup(request):
    return render(request, "register.html")
