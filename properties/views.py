from django.shortcuts import render
from django.db.models import Max
from .models import Property, Type, County


def properties(request):
    """ A view to show all products, including sorting and search queries """

    properties = Property.objects.all()
    property_type = Type.objects.all()
    counties = County.objects.all()

    if request.GET:
        prop_type = request.GET['prop-type']
        county = request.GET['county']
        price_min = request.GET['price-min']
        price_max = request.GET['price-max']
        beds_min = request.GET['beds-min']
        beds_max = Property.objects.aggregate(Max('bedrooms'))['bedrooms__max']
                   
        properties = Property.objects.filter(property_type=prop_type, county=county, price__range=(price_min, price_max), bedrooms__range=(beds_min, beds_max))
    

    context = {
        'properties': properties,
        'property_type': property_type,
        'counties': counties,
    }

    return render(request, 'properties/properties.html', context)
