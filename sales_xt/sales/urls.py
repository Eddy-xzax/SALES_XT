from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserList, ProductViewSet
from . import views
from .views import product_report
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('users/', UserList.as_view(), name='user-list'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('product-report/', product_report, name='product-report'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

