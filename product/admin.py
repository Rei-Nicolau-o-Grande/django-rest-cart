from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'price', 'score', 'image'
    list_display_links = 'name',
    search_fields = 'name', 'price', 'score'


admin.site.register(Product, ProductAdmin)