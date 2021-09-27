from django.db import models
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'price',
            'brand',
            'id_supplier',
            'id_category_product'
        ]


