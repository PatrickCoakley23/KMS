from django.shortcuts import render
from .models import Property


# Create your views here.

def properties(request):
    """ a view to return the properties page """

    properties = Property.objects.all()

    context = {
        'properties': properties,
    }

    return render(request, 'properties/properties.html', context)