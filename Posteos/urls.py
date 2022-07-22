from django.urls import path
from Posteos import views

urlpatterns = [
    path('', views.home, name='bienvenida'),
    path('crearpost/', views.crearPost, name='crearPost'),
    
]