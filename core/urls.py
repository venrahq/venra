from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
    path('contact/', views.contact, name='contact'),
]