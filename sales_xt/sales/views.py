from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def home(request):
 #   return HttpResponse("Welcome, To the Sales xt app.")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")


