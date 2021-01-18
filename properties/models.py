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
    
    BER_RATING_CHOICES = (
        ('A1', ('A1')),
        ('A2', ('A2')),
        ('A3', ('A3')),
        ('B1', ('B1')),
        ('B2', ('B2')),
        ('B3', ('B3')),
        ('C1', ('C1')),
        ('C2', ('C2')),
        ('C3', ('C3')),
        ('D1', ('D1')),
        ('D2', ('D2')),
        ('E1', ('E1')),
        ('E2', ('E2')),
        ('FG', ('FG')),
        ('Exempt', ('EXEMPT')),
    )

    name = models.CharField(max_length=254)
    property_type = models.ForeignKey('Type', null=True,
                                      blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=254)
    county = models.ForeignKey('County', null=True,
                               blank=True, on_delete=models.SET_NULL)
    latitude = models.DecimalField(max_digits=25, decimal_places=5, null=False, blank=False)
    longitude = models.DecimalField(max_digits=25, decimal_places=5, null=False, blank=False)
    description = models.TextField()
    bedrooms = models.DecimalField(max_digits=3, decimal_places=0)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    size = models.DecimalField(max_digits=8, decimal_places=0)
    ber_rating = models.CharField(max_length=10, choices=BER_RATING_CHOICES, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.property.name
        
