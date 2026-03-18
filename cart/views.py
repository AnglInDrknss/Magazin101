from PIL.Image import item
from django.shortcuts import render
from requests import session

from product.models import Product
from .models import Cart, CartItem
from .serializers import CartSerializer
from rest_framework import request, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from cart.serializers import CartActionSerializer

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_cart(self, request):
        if not request.session.session_key:
            request.session.create()
        cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
        return cart

    def list(self, request):
        cart = self.get_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)

    @action(detail=False, methods=["post"], serializer_class=CartActionSerializer)
    def add_product(self, request):
        serializer = CartActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart = self.get_cart(request) 
        product_id = serializer.validated_data['product_id']
        quantity = serializer.validated_data.get('quantity', 1)

        cart.add_product(product_id, quantity)  

        return Response({"message": "Product added"})

    @action(detail=False, methods=["post"], serializer_class=CartActionSerializer)
    def remove(self, request):
        serializer = CartActionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        cart = self.get_cart(request)
        cart.remove_product(serializer.validated_data['product_id'])
        return Response({"message": "Product removed"})