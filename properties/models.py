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


class Agent(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.EmailField(max_length=254)
    image = models.ImageField(null=True, blank=True)

    def clean(self):
        self.name = self.name.capitalize()
        self.position = self.position.capitalize()

    def __str__(self):
        return self.name


class Ber_Rating(models.Model):
    name = models.CharField(max_length=10)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Property(models.Model):
    SALE_STATUS_CHOICES = (
        ('For Sale', ('For Sale')),
        ('Sale Agreed', ('Sale Agreed')),
        ('Sold', ('Sold')),
    )

    name = models.CharField(max_length=254)
    property_type = models.ForeignKey('Type', null=True,
                                      blank=True, on_delete=models.SET_NULL)
    address = models.CharField(max_length=254)
    county = models.ForeignKey('County', null=True,
                               blank=True, on_delete=models.SET_NULL)
    latitude = models.DecimalField(
        max_digits=25, decimal_places=20,
        null=False, blank=False, help_text="Navigate to Google's Maps, "
        "Enter the address you want to find, "
        "Right click on the Map's pin point and the lat-lng will appear. "
        "Latitude is the first number, longitude is second. "
        "eg. (51.89371, -8.49649) (latitude, longitude)")
    longitude = models.DecimalField(
        max_digits=25, decimal_places=20,
        null=False, blank=False,)
    description = models.TextField()
    bedrooms = models.DecimalField(max_digits=3, decimal_places=0)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=8,
                                decimal_places=0,
                                help_text="Put price as 5000000 "
                                "if you want 'Price Upon Request'")
    sqm = models.DecimalField(max_digits=8, decimal_places=0,
                              blank=True, null=True,
                              help_text="if acres leave blank")
    acres = models.DecimalField(max_digits=8, decimal_places=0,
                                blank=True, null=True,
                                help_text="if sqm leave blank")
    description = models.TextField()
    ber_rating = models.ForeignKey(
        'Ber_Rating', null=True,
        blank=True, on_delete=models.SET_NULL)
    image = models.ImageField(null=True, blank=True)
    youtube_id = models.CharField(max_length=1024,
                                 null=True, blank=True,
                                 help_text="Requires the ID of youtube video "
                                 "Not the full url. "
                                 "ID is the last part of the url eg. "
                                 "https://www.youtube.com/watch?v=ZIOCKqk4x3A "
                                 "the ID here is "
                                 "ZIOCKqk4x3A ")
    matterport_id = models.CharField(max_length=1024, null=True, blank=True,
                                     help_text="Requires the ID of matterport video "
                                     "Not the full url. "
                                     "ID is the last part of the url eg. "
                                     "https://my.matterport.com/show/?m=PhqeQDhKBYd "
                                     "the ID here is "
                                     "PhqeQDhKBYd ")
    date_added = models.DateTimeField(auto_now_add=False)
    agent = models.ForeignKey(
        'Agent', null=True, blank=True,
        on_delete=models.SET_NULL)
    sale_status = models.CharField(
        max_length=30, choices=SALE_STATUS_CHOICES, default="For Sale",)

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name


class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property, default=None, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.property.name
