from django.urls import path
from AmorFati.sitedelivery import views

app_name = 'sitedelivery'

urlpatterns = [
    path('', views.home, name='home'),
]
