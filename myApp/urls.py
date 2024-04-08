

# urls.py

from django.urls import path
from .views import home, about, services, contact 

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('contact/', contact, name='contact'),
    # Add other URL patterns here if needed
]

# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Add more URL patterns as needed
]
