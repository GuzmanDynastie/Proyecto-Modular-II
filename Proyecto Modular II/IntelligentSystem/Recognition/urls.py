from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_scan, name='product_scan'),
    path('video/', views.video, name='video'),
    path('home/', views.stop_video, name='stop'),
]