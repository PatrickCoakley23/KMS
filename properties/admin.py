from django.contrib import admin
from .models import Property, Type, County, PropertyImage, Agent, Ber_Rating


class PropertyImageAdmin(admin.StackedInline):
    model = PropertyImage


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('combine_name_and_address', 'county',
                    'property_type',
                    'price', 'sale_status')
    list_filter = ('property_type',)
    search_fields = ('name', 'address')
    inlines = [PropertyImageAdmin]

    class Meta:
        model = Property

    def combine_name_and_address(self, obj):
        return "{}, {}".format(obj.name, obj.address)


admin.site.register(Property, PropertyAdmin)


class PropertyImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(PropertyImage, PropertyImageAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Type, TypeAdmin)
admin.site.register(County)
admin.site.register(Agent)
admin.site.register(Ber_Rating)
