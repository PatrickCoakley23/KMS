from django.shortcuts import render
from .models import Property, Type, County


def properties(request):
    """ A view to show all products, including sorting and search queries """

    properties = Property.objects.all()
    property_type = Type.objects.all()
    counties = County.objects.all()

    context = {
        'properties': properties,
        'property_type': property_type,
        'counties': counties,
    }

    return render(request, 'properties/properties.html', context)
