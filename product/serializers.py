from django.db.models import Q
from rest_framework import serializers
from product.models import Category, SubCategory, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'icon', 'created_at']


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'icon', 'description', 'category', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'sub_category', 'sort_order', 'created_at', 'updated_at']


