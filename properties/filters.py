import django_filters

from .models import Property, Type, County


class PropertyFilter(django_filters.FilterSet):
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Min Price')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Max Price')
    bedrooms_gte = django_filters.NumberFilter(field_name='bedrooms', lookup_expr='gte', label='Min Beds')

    class Meta:
        model = Property
        fields = [
            'property_type',
            'county',
        ]

