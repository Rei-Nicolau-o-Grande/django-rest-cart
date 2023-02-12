import django_filters

from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = django_filters.OrderingFilter(fields=['name', 'score', 'price'])

    class Meta:
        model = Product
        fields = ['name']