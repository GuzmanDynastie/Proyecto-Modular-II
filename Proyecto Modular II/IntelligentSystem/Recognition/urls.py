from django.urls import path
from . import views

urlpatterns = [
    path('', views.recognition_home_view, name='recognition_home'),
    path('video/', views.video, name='video'),
]