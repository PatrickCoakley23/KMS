from django.shortcuts import render
from .models import Testimonial
from properties.models import Agent

from .forms import ContactForm

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


def Contact(request):
    """ a view to return the contact page"""

    contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
    }

    return render(request, "home/contact.html", context)
