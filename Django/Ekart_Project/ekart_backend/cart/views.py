from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer

@api_view(['GET','POST'])
def product_list_create(request):
    if request.method == 'GET':
        products= Product.objects.all()
        serializer= ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method== 'POST':
        serializer= ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def cart_list_create(request):
    if request.method == 'GET':
        cart_items = CartItem.objects.all()
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def cart_delete(request, pk):
    try:
        item = CartItem.objects.get(pk=pk)
    except CartItem.DoesNotExist:
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({'message': 'Item removed from cart'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['DELETE'])
def product_delete(request, pk):
    try:
        item = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        print("Inside Except!")
        return Response({'error': 'Item not found'}, status=status.HTTP_404_NOT_FOUND)

    item.delete()
    return Response({'message': 'Item removed from Product'}, status=status.HTTP_204_NO_CONTENT)

