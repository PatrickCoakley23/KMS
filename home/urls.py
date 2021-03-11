from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('kms/', views.index, name='home'),
    path('selling_guide/', views.SellingGuide, name='SellingGuide'),
    path('contact/', views.Contact, name='ContactUs'),
]
