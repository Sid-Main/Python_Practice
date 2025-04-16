from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CartItem
from .serializers import CartItemSerializer
from products.models import Product
from rest_framework.permissions import IsAuthenticated

# View to handle Cart Item operations (CRUD)
class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Return all cart items for the logged-in user
    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    # Create a new cart item (when user adds a product to their cart)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        cart_items = CartItem.objects.filter(user=user)

        if not cart_items:
            return Response({'message': 'Your cart is empty.'}, status=status.HTTP_400_BAD_REQUEST)

        total_amount = 0
        for cart_item in cart_items:
            product = cart_item.product
            quantity = cart_item.quantity

            if product.inventory < quantity:
                return Response(
                    {'message': f"Insufficient stock for {product.name}. Available: {product.inventory}"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            total_amount += product.price * quantity
            product.inventory -= quantity
            product.save()

        cart_items.delete()

        return Response({'message': 'Purchase successful!', 'total_amount': total_amount}, status=status.HTTP_200_OK)


