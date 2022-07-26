from django.urls import path
from Posteos import views

urlpatterns = [
    path('', views.BienvenidaView.as_view(), name='bienvenida'), # ListView
    path('crearpost/', views.crearPost, name='crearPost'),
    #path('crearpost/', views.EntradaCreacion.as_view(), name='crearPost'),   # No funciona!!!!  
    path('buscar/', views.buscar, name='buscar'),
    path('verEntrada/<int:id>', views.verPost, name='verEntrada'),
    #path('verEntrada/<int:id>', views.EntradaDetalle.as_view(), name='verEntrada'),      # DetailView       # No funciona!!!!   
    path('editarEntrada/<int:id>', views.editarPost, name='editarEntrada'),          # Funciona, pero me duplica las entradas y no puedo resolver lo del id
    path('eliminarEntrada/<int:id>', views.eliminarPost, name='eliminarEntrada'),
    


    path('test/', views.test, name='test'),
    
    
]