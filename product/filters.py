import django_filters

from .models import Product

class ProductFilter(django_filters.FilterSet):
    #price = django_filters.OrderingFilter(fields=['price'])
    score = django_filters.OrderingFilter(fields=['score', 'price'])

    class Meta:
        model = Product
        fields = ['score']