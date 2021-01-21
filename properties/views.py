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

    paginator = Paginator(propFilter.qs, 15)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)

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

    ber_rating = property.ber_rating

    if ber_rating == 'A1':
        ber_image = 'A1_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'A2':
        ber_image = 'A2_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'A3':
        ber_image = 'A3_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'B1':
        ber_image = 'B1_BER_RGB_Web_and_PC.png'
    
    elif ber_rating == 'B2':
        ber_image = 'B2_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'B3':
        ber_image = 'B3_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'C1':
        ber_image = 'C1_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'C2':
        ber_image = 'C2_BER_RGB_Web_and_PC.png'
    
    elif ber_rating == 'C3':
        ber_image = 'C3_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'D1':
        ber_image = 'D1_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'D2':
        ber_image = 'D2_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'E1':
        ber_image = 'E1_RGB_BER.png'

    elif ber_rating == 'E2':
        ber_image = 'E2_RGB_BER.png'

    elif ber_rating == 'F':
        ber_image = 'F_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'G':
        ber_image = 'G_BER_RGB_Web_and_PC.png'

    elif ber_rating == 'Exempt':
        ber_image = 'BER-exempt.png'

    context = {
        'property': property,
        'images': images,
        'lat': lat,
        'lng': lng,
        'google_api_key': google_api_key,
        'ber_image' : ber_image,
    }

    return render(request, 'properties/property_selected.html', context)
