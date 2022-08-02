from django.urls import path
from Posteos import views
from .views import EntradaDetailView, EntradaCreateView, EntradaUpdateView, EntradaDeleteView

urlpatterns = [
    path('', views.BienvenidaView.as_view(), name='bienvenida'), # ListView

    path('buscar/', views.buscar, name='buscar'),

    path('entrada/<pk>', EntradaDetailView.as_view(), name='entrada-detail'), #DetailView
    # Deprecated path('verEntrada/<int:id>', views.verPost, name='verEntrada'),
      
    path('crearpost/', EntradaCreateView.as_view(), name ="entrada-create"), #CreateView
    # Deprecated path('crearpost/', views.crearPost, name='crearPost'),

    path('entrada/<pk>/update', EntradaUpdateView.as_view(), name ="entrada-update"), #UpdateView
    # Deprecated path('editarEntrada/<int:id>', views.editarPost, name='editarEntrada'),        

    path('eliminarEntrada/<pk>', EntradaDeleteView.as_view(), name ="entrada-delete" ), #DeleteView
    # Deprecated path('eliminarEntrada/<int:id>', views.eliminarPost, name='eliminarEntrada'),
    

# Eliminarlo antes de la entrega final
    path('test/', views.test, name='test'),

]