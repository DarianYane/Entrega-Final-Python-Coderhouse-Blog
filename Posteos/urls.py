from django.urls import path
from Posteos import views

urlpatterns = [
    path('', views.home, name='bienvenida'),
    path('crearpost/', views.crearPost, name='crearPost'),
    path('buscar/', views.buscar, name='buscar'),
    # path('buscar/', views.formulario_busqueda, name='formulario_busqueda'),
    path('eliminarEntrada/<int:id>', views.eliminarPost),
    path('editarEntrada/<int:id>', views.editarPost),


    path('test/', views.test, name='test'),
    
    
]