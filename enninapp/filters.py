import django_filters
from django_filters import CharFilter


from django import forms

from .models import Product

class ProductFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr="icontains", label="Search")

    class Meta:
        model = Product
        fields = ['name', 'brand']