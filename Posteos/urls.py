from django.urls import path
from Posteos import views
from .views import EntradaDetailView, EntradaCreateView, EntradaUpdateView, EntradaDeleteView

urlpatterns = [
    path('', views.BienvenidaView.as_view(), name='bienvenida'), # ListView
    path('buscar/', views.buscar, name='buscar'),
    path('entrada/<pk>', EntradaDetailView.as_view(), name='entrada-detail'), #DetailView
    path('crearpost/', EntradaCreateView.as_view(), name ="entrada-create"), #CreateView
    path('entrada/<pk>/update', EntradaUpdateView.as_view(), name ="entrada-update"), #UpdateView
    path('eliminarEntrada/<pk>', EntradaDeleteView.as_view(), name ="entrada-delete" ), #DeleteView
    path('como_utilizar_el_blog/', views.como_utilizar_el_blog, name='como_utilizar_el_blog'),
    path('quienes_somos/', views.quienes_somos, name='quienes_somos'),

]