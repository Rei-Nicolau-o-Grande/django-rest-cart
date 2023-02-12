from rest_framework import serializers

from .models import Product, Cart, ItemCart

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'score', 'image')

class ItemCartSerializer(serializers.ModelSerializer):
    total_price = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = ItemCart
        fields = 'id', 'cart', 'product', 'quantity', 'total_price', 'created_at', 'updated_at'


class CartSerializer(serializers.ModelSerializer):
    items = ItemCartSerializer(many=True, read_only=False)
    shipping_cost = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    subtotal = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    total = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)

    class Meta:
        model = Cart
        fields = 'id', 'user', 'items', 'shipping_cost', 'subtotal', 'total', 'created_at', 'updated_at'

