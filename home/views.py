from django.shortcuts import render
from .models import Testimonial

# Create your views here.

def index(request):
    """ a view to return the index page """
    testimonials = Testimonial.objects.all()

    context = {
        'testimonials': testimonials
    }

    return render(request, 'home/index.html', context)