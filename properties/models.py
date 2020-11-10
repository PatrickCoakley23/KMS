from django.db import models

class Type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def __get_friendly_name(self):
        return self.friendly_name

class County(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=254)
    type = models.ForeignKey('Type', null=True, blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=254)
    county = models.ForeignKey('County', null=True, blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    bedrooms = models.TextField()
    bathrooms = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=0)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    ber_rating = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



