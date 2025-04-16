# cart/urls.py
from django.urls import path, include
from .views import CartItemViewSet, CheckoutView
from rest_framework.routers import DefaultRouter

# Set up a default router to handle the cart item endpoints
router = DefaultRouter()
router.register(r'cart', CartItemViewSet, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('checkout/', CheckoutView.as_view(), name='checkout'),  # Checkout endpoint
]
