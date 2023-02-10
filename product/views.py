from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializers

from .pagination import Pagination

from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter
