from django.test import TestCase


class TestViews(TestCase):

    def test_properties_page(self):
        response = self.client.get('/properties/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/properties.html')


