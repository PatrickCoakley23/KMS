from django.shortcuts import render
from .models import Testimonial
from properties.models import Agent

# Create your views here.

def index(request):
    """ a view to return the index page """
    testimonials = Testimonial.objects.all()
    agents = Agent.objects.all()

    context = {
        'testimonials': testimonials,
        'agents': agents,
    }

    return render(request, 'home/index.html', context)

def SellingGuide(request):
    """ a view to return the selling guide """

    return render(request, "home/selling_guide.html")
