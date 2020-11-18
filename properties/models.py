from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class County(models.Model):

    class Meta:
        verbose_name_plural = 'Counties'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Property(models.Model):

    class Meta:
        verbose_name_plural = 'Properties'

    name = models.CharField(max_length=254)
    property_type = models.ForeignKey('Type', null=True,
                                      blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=254)
    county = models.ForeignKey('County', null=True,
                               blank=True, on_delete=models.SET_NULL)
    description = models.TextField()
    bedrooms = models.DecimalField(max_digits=3, decimal_places=0)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    size = models.DecimalField(max_digits=8, decimal_places=2)
    ber_rating = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
