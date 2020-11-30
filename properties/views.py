from django.shortcuts import render
from django.db.models import Max
from .models import Property, Type, County
from .filters import PropertyFilter


def properties(request):
    """ A view to show all products, including sorting and search queries """

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


    context = {
    'filter': propFilter
}
  
    return render(request, 'properties/properties.html', context )
