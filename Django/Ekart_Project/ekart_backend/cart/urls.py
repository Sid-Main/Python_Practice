from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.product_list_create, name='product-list-create'),
    path('cart/', views.cart_list_create, name='cart-list-create'),
    path('cart/<int:pk>/', views.cart_delete, name='cart-delete'),
    path('products/<int:pk>/', views.product_delete, name='product-delete'),
]