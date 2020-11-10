from django.contrib import admin
from .models import Property, Type, County


class PropertyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'property_type',
        'address',
        'price',
        'bedrooms',
        'image',
    )

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Property, PropertyAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(County)

