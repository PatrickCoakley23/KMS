from django import forms

import django_filters

from .models import Property, Type, County


class PropertyFilter(django_filters.FilterSet):
    property_type = django_filters.ModelChoiceFilter(queryset=Type.objects.all(), empty_label="All", label="")
    county = django_filters.ModelChoiceFilter(queryset=County.objects.all(), empty_label="All", label="")
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label="")
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label="")
    bedrooms__gte = django_filters.NumberFilter(field_name='bedrooms', lookup_expr='gte', label="")
    

    class Meta:
        model = Property
        fields = [
            'property_type',
            'county',
            'price__gte',
            'price__lte',
            'bedrooms__gte'
        ]

