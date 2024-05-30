from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
    path('criar/', views.criar_reserva, name='criar_reserva'),
    path('minhas/', views.minhas_reservas, name='minhas_reservas'),
]