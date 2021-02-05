from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Property, PropertyImage
from .filters import PropertyFilter
from django.conf import settings
from django.db.models.functions import Lower


def properties(request):
    """ A view to show all products, including sorting and search queries """
    context = {}
    properties = Property.objects.all().order_by('?')
    propFilter = PropertyFilter(request.GET, queryset=properties)
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            if sortkey == 'name':
                sortkey = 'lower_name'
                properties = Property.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            properties = properties.order_by(sortkey)
            propFilter = PropertyFilter(request.GET, queryset=properties)

    paginator = Paginator(propFilter.qs, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

    context = {
        'filter': propFilter,
        'page_obj': page_obj
    }

    return render(request, 'properties/properties.html', context)


def property_selected(request, properties_id):
    """ A view that gives more details on the property selected """

    property = get_object_or_404(Property, pk=properties_id)
    images = PropertyImage.objects.filter(property=property)
    google_api_key = settings.GOOGLE_API_KEY
    lat = property.latitude
    lng = property.longitude

    referer = str(request.META.get('HTTP_REFERER'))
    host = str(request.META.get('HTTP_HOST'))

    if host in referer:
        referer = request.META.get('HTTP_REFERER')
    else:
        referer = None

    context = {
        'property': property,
        'images': images,
        'lat': lat,
        'lng': lng,
        'google_api_key': google_api_key,
        'referrer': referer,
    }

    return render(request, 'properties/property_selected.html', context)
