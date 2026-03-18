from django.shortcuts import redirect, get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from product.models import Product, SocialMedia, SubCategory, Category
from product.serializers import (
    CategorySerializer, SocialMediaSerializer, SubCategorySerializer,
    ProductSerializer
)
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

    @action(detail=False, methods=['get'], url_path='by-category')
    def by_category(self, request):
        category_id = request.query_params.get('category_id')

        if not category_id:
            return Response({"error": "category_id is required"}, status=400)

        subcategories = SubCategory.objects.filter(category_id=category_id)
        serializer = self.get_serializer(subcategories, many=True)

        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'price', 'sort_order', 'created_at', 'updated_at', 'sub_category__name']
    ordering = ['sort_order', 'name']

    @action(detail=False, methods=['get'], url_path='by-subcategory')
    def by_subcategory(self, request):
        subcategory_id = request.query_params.get('subcategory_id')

        if not subcategory_id:
            return Response({"error": "subcategory_id is required"}, status=400)

        products = Product.objects.filter(sub_category_id=subcategory_id)
        serializer = self.get_serializer(products, many=True)

        return Response(serializer.data)


class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

