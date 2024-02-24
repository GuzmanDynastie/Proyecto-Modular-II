from django.urls import path
from . import views

urlpatterns = [
    path('', views.imprimir),
    path('about/', views.acerca),
]