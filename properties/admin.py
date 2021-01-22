from django.contrib import admin
from .models import Property, Type, County, PropertyImage, Agent, Ber_Rating

class PropertyImageAdmin(admin.StackedInline):
    model=PropertyImage

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageAdmin]

    class Meta:
        model=Property

@admin.register(PropertyImage)
class PropertyImageAdmin(admin.ModelAdmin):
    pass

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Type, TypeAdmin)
admin.site.register(County)
admin.site.register(Agent)
admin.site.register(Ber_Rating)



