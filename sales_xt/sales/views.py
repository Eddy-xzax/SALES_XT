from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
#
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import generics

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


#@api_view(["POST"])
#def register(request):
    #username = request.data.get("username")
    #email = request.data.get("email")
    #password = request.data.get("password")

    #if User.objects.filter(username=username).exists():
        #return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

    #user = User.objects.create_user(username=username, email=email, password=password)
    #token, _ = Token.objects.get_or_create(user=user)

    #return Response({
        #"message": "User created successfully",
        #"token": token.key
    #}, status=status.HTTP_201_CREATED)

#class CustomUserViewSet(viewsets.ModelViewSet):
    #queryset = CustomUser.objects.all()
    #serializer_class = CustomUserSerializer

#class SignUpView(CreateView):
#   form_class = CustomUserCreationForm
#  success_url = reverse_lazy("login")
# template_name = "registration/registration.html"
#hope this works cause  if it doest am cooked

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#def login(request):
    #return render(request, "login.html")

#def signup(request):
    #return render(request, "register.html")

def product_report(request):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="product_report.pdf"'

    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    
    y = height - 50
    p.setFont("Helvetica-Bold", 14)
    p.drawString(180, y, "Product Profit Report")

    
    y -= 40
    p.setFont("Helvetica-Bold", 12)
    p.drawString(50, y, "Name")
    p.drawString(200, y, "Description")
    p.drawString(400, y, "Profit")

    
    y -= 30
    p.setFont("Helvetica", 12)
    products = Product.objects.all()

    for product in products:
        profit = product.profit() if product.buying_price and product.selling_price else 0

        p.drawString(50, y, product.name or "N/A")
        p.drawString(200, y, (product.description[:30] + "...") if product.description else "N/A")
        p.drawString(400, y, f"{profit:.2f}")

        y -= 25
        
        if y < 50:
            p.showPage()
            y = height - 50
            p.setFont("Helvetica-Bold", 12)
            p.drawString(50, y, "Name")
            p.drawString(200, y, "Description")
            p.drawString(400, y, "Profit")
            y -= 30
            p.setFont("Helvetica", 12)

    
    p.showPage()
    p.save()
    return response
