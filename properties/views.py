from django.shortcuts import render
from django.db.models import Max
from .models import Property, Type, County
from .filters import PropertyFilter


def properties(request):
    """ A view to show all products, including sorting and search queries """

    properties = Property.objects.all()
    propFilter = PropertyFilter(request.GET, queryset=properties)

    context = {
    'filter': propFilter
}
  

    return render(request, 'properties/properties.html', context )
