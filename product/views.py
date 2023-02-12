from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Product, Cart, ItemCart
from .serializers import ProductSerializer, CartSerializer, ItemCartSerializer

from .pagination import Pagination

from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter


class ListProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = Pagination
    permission_classes = [IsAuthenticated, ]

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

class CartApi(ModelViewSet):

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'user'

    permission_classes = [IsAuthenticated, ]

    def get_queryset(self):
        user = self.request.user
        queryset = Cart.objects.filter(user=user)
        return queryset


@api_view(http_method_names=['post'])
@permission_classes(permission_classes=[IsAuthenticated])
def item_cart_post(request):

    if request.method == 'POST':
        serializer = ItemCartSerializer(
            data=request.data,
            context={'request': request},
        )
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(http_method_names=['delete'])
@permission_classes(permission_classes=[IsAuthenticated])
def item_cart_delete(request, pk):
    qs = get_object_or_404(ItemCart, pk=pk)

    if request.method == 'DELETE':
        qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

