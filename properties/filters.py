from django import forms

import django_filters

from .models import Property, Type, County


class PropertyFilter(django_filters.FilterSet):
    PRICE_CHOICES = (
        (100000, ('€100,000')),
        (200000, ('€200,000')),
        (300000, ('€300,000')),
        (400000, ('€400,000')),
        (500000, ('€500,000')),
        (600000, ('€600,000')),
        (700000, ('€700,000')),
        (800000, ('€800,000')),
        (900000, ('€900,000')),
        (1000000, ('€1m')),
        (1500000, ('€1.5m')),
        (2000000, ('€2m')),
        (3000000, ('€3m')),
        (4000000, ('€4m')),
        (5000000, ('€5m')),
    )

    BED_CHOICES = (
        (1, ('1')),
        (2, ('2')),
        (3, ('3')),
        (4, ('4')),
        (5, ('5+')),
    )

    property_type = django_filters.ModelChoiceFilter(queryset=Type.objects.all(), empty_label="All", label="")
    county = django_filters.ModelChoiceFilter(queryset=County.objects.all(), empty_label="All", label="")
    price__gte = django_filters.ChoiceFilter(choices=PRICE_CHOICES, field_name='price', lookup_expr='gte', label="", empty_label="No Min")
    price__lte = django_filters.ChoiceFilter(choices=PRICE_CHOICES, field_name='price', lookup_expr='lte', label="", empty_label="No Max")
    bedrooms__gte = django_filters.ChoiceFilter(choices=BED_CHOICES, field_name='bedrooms', lookup_expr='gte', label="", empty_label="No Min" )
   
    

    class Meta:
        model = Property
        fields = [
            'property_type',
            'county',
            'price__gte',
            'price__lte',
            'bedrooms__gte'
        ]

