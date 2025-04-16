from rest_framework import serializers
from .models import CartItem
from products.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    price = serializers.ReadOnlyField(source='product.price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity']

    def validate(self, data):
        product = data['product']
        quantity = data['quantity']

        if quantity > product.inventory:
            raise serializers.ValidationError(f"Only {product.inventory} items available in stock.")
        return data
