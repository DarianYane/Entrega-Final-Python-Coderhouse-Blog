from django.urls import path
from Posteos import views

urlpatterns = [
    path('', views.home, name='bienvenida'),
    path('crearpost/', views.crearPost, name='crearPost'),
    path('buscar/', views.buscar, name='buscar'),
    # path('buscar/', views.formulario_busqueda, name='formulario_busqueda'),



    path('test/', views.test, name='test'),
    
    
]