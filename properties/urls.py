from django.urls import path
from . import views

urlpatterns = [
    path('', views.properties, name='properties'),
    path('<properties_id>', views.property_selected, name='property_selected'),
]
