from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):

    def test_name_is_required(self):
        form = ContactForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_phone_number_is_not_required(self):
        form = ContactForm({'name': 'Testing Contactform',
                            'email': 'test@gmail.com',
                            'subject': 'new house',
                            'message': 'hello test',
                            })
        self. assertTrue(form.is_valid())


