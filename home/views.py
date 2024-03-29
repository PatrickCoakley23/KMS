from django.shortcuts import render, redirect
from .models import Testimonial
from properties.models import Agent
from .forms import ContactForm

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import get_template

import requests
# Create your views here.

def index(request):
    """ a view to return the index page """
    testimonials = Testimonial.objects.all().order_by('-date_published')
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

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = request.POST.get('name', '')
            email_address = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            phone_number = request.POST.get('phone_number', '')
            message = request.POST.get('message', '')
            template = get_template('home/contact_template.txt')

            context = {
                'name': name,
                'email_address': email_address,
                'subject': subject,
                'phone_number': phone_number,
                'message': message,
            }
            content = template.render(context)

            email = EmailMessage(
                'Contact-Form ' + subject,
                content,
                email_address,
                ['keanemahonysmith@gmail.com'],
            )

            ''' Begin reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response
            }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()
            ''' End reCAPTCHA validation '''

            if result['success']:
                email.send()
                messages.success(request, f'Thanks {name}, Your Contact Form Has '
                                      'Been Successfully Sent.')
            else:
                messages.error(request, 'Invalid reCAPTCHA. Please try again.')

            return redirect('ContactUs')

    google_site_key = settings.GOOGLE_RECAPTCHA_SITE_KEY

    context = {
        'contact_form': contact_form,
        'google_site_key': google_site_key,
    }

    return render(request, "home/contact.html", context)
