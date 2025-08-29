from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet,ProductViewSet
from . import views

router = DefaultRouter()
router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'products', ProductViewSet)

urlpatterns = [
  #  path("", views.home, name="home"),
  #  path("login/", views.login, name = "login"),
  #  path("signup/", views.signup, name = "signup"),
  #  path('', include(router.urls)),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
#    path('api/token/', obtain_auth_token),
]
