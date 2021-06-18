from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('crear_post/', views.crear_post),
    path('ver_detalle/<int:id_post>',views.ver_detalle),
    path('editar/<int:id_post>',views.editar),
    path('eliminar/<int:id_post>',views.eliminar),
    path('like/<int:id_post>',views.like),
    path('unlike/<int:id_post>',views.unlike),
]
