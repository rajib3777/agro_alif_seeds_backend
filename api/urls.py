from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, OrderViewSet, ArticleViewSet, ContactMessageViewSet
from .views import phone_login, phone_register

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'messages', ContactMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', phone_login, name='phone-login'),
    path('auth/register/', phone_register, name='phone-register'),
]
