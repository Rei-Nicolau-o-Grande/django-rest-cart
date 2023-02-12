from django.contrib import admin

from .models import Product, Cart, ItemCart

class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'score', 'image'
    list_display_links = 'name',
    search_fields = 'name', 'price', 'score'

class CartAdmin(admin.ModelAdmin):
    list_display = 'id', 'user', 'shipping_cost', 'subtotal', 'total', 'created_at', 'updated_at',
    list_display_links = 'id', 'user'

class ItemCartAdmin(admin.ModelAdmin):
    list_display = 'id', 'product', 'quantity', 'total_price', 'created_at', 'updated_at'
    list_display_links = 'id', 'product'


admin.site.register(Product, ProductAdmin)

admin.site.register(Cart, CartAdmin)

admin.site.register(ItemCart, ItemCartAdmin)