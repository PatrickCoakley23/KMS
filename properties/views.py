from django.shortcuts import render
from .models import Property
# Create your views here.

def properties(request):
    """ A view to show all products, including sorting and search queries """

    properties = Property.objects.all()

    context = {
        'properties': properties,
    }

    return render(request, 'properties/properties.html', context)