from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crear_post/', views.crear_post),
]
