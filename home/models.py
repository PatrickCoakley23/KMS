from django.db import models


# Create your models here.
class Testimonial(models.Model):
    clients_name = models.CharField(max_length=254)
    comment = models.TextField(max_length=350)
    date_published = models.DateField(null=False)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.clients_name