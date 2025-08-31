from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserList, ProductViewSet
from . import views
from .views import product_report
#from .views import register
router = DefaultRouter()
#router.register(r'users', CustomUserViewSet, basename='user')
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', UserList.as_view(), name='User-list'),
  #  path("", views.home, name="home"),
  #  path("login/", views.login, name = "login"),
  #  path("signup/", views.signup, name = "signup"),
    path('', include(router.urls)),
    path("api/", include(router.urls)),
  #  path("api/register/", register, name="register"),
  #  path('api-auth/', include('rest_framework.urls')),
    path("product-report/", views.product_report, name="product_report"),
#    path('api/token/', obtain_auth_token),
]
