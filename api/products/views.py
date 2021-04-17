from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from products.serializers import ProductSerializer


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
