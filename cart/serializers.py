from rest_framework import serializers
from models import Cart, CartItem

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.name")
    price = serializers.DecimalField(source="product.price", max_digits=10, decimal_places=2)

    class Meta:
        model = CartItem
        fields = ["product", "product_name", "price", "quantity"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(source="cartitem_set", many=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "items", "total_price"]

    def get_total_price(self, obj):
        return obj.get_total_price()
    

class CartActionSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(required=False, default=1)