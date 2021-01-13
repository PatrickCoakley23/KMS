from django.shortcuts import render, get_object_or_404
from django.db.models import Max
from django.core.paginator import Paginator
from .models import Property, Type, County, PropertyImage
from .filters import PropertyFilter
from django.conf import settings


def properties(request):
    """ A view to show all products, including sorting and search queries """
    context = {}
    properties = Property.objects.all()
    propFilter = PropertyFilter(request.GET, queryset=properties)
    sort = None 
    direction = None 
    
    if request.GET: 
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                properties = Property.annotate(lower_name=Lower('name'))
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            properties = properties.order_by(sortkey)
            propFilter = PropertyFilter(request.GET, queryset=properties)

    paginated_properties = Paginator(propFilter.qs, 4)
    page_number = request.GET.get('page')
    page_obj = paginated_properties.get_page(page_number)

    context = {
    'filter': propFilter, 
    'page_obj': page_obj
    }
  
    return render(request, 'properties/properties.html', context )


    
def property_selected(request, properties_id): 
    """ A view that gives more details on the property selected """

    property = get_object_or_404(Property, pk=properties_id)
    images = PropertyImage.objects.filter(property=property)
    google_api_key = settings.GOOGLE_API_KEY
    lat = property.latitude
    lng = property.longitude
    context = {
        'property': property,
        'images': images,
        'lat': lat,
        'lng': lng,
        'google_api_key': google_api_key
    }

    return render(request, 'properties/property_selected.html', context)
