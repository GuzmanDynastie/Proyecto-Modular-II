from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_scan, name='product_scan'),
    path('video/', views.video, name='video'),
    path('stop_video/', views.stop_video, name='stop_video'),
    path('restart_video/', views.restart_video, name='restart_video'),
]