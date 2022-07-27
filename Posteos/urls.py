from django.urls import path
from Posteos import views

#importar clase del profesor
from .views import EntradaDetailView, EntradaCreateView

urlpatterns = [
    path('', views.BienvenidaView.as_view(), name='bienvenida'), # ListView




    path('buscar/', views.buscar, name='buscar'),

        #Path del profesor
    path('entrada/<pk>', EntradaDetailView.as_view(), name='entrada-detail'), #DetailView
    # Deprecated path('verEntrada/<int:id>', views.verPost, name='verEntrada'),
      
    path('crearpost/', EntradaCreateView.as_view(), name ="entrada-create" ), #CreateView
    # Deprecated path('crearpost/', views.crearPost, name='crearPost'),


    path('editarEntrada/<int:id>', views.editarPost, name='editarEntrada'),          # Funciona, pero me duplica las entradas y no puedo resolver lo del id
    
    path('eliminarEntrada/<int:id>', views.eliminarPost, name='eliminarEntrada'),
    


    path('test/', views.test, name='test'),


#Path del profesor sin probar


#    path('article/<pk>/update', ArticleUpdateView.as_view(), name ="article-update" ),
#    path('article/<pk>/delete', ArticleDeleteView.as_view(), name ="article-delete" ),
    

]