from django.shortcuts import render
from Posteos.models import Entrada
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .forms import EntradaForm


#Eliminar este de testeos antes de entregar el trabajo
def test(request):
    #posteos = Entrada.objects.all()
    return render(request, 'test.html')



def buscar(request):
    if request.GET["titulo"]:
        queryset = request.GET["titulo"]       
        entradas = Entrada.objects.filter(titulo__icontains=queryset).all()

        if entradas!=[]:
            return render(request, "busqueda_entrada.html", {"entradas": entradas, "titulo": queryset})

    else:
        queryset = "(No realizó búsqueda)"
        return render(request, "busqueda_entrada.html", {"titulo": queryset})


class BienvenidaView(ListView):
    queryset = Entrada.objects.all()
    context_object_name = "posteos"
    template_name = "bienvenida.html"


class EntradaDetailView(DetailView):
    model = Entrada
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class EntradaCreateView(CreateView):
    model = Entrada
    #fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'creado']
    form_class = EntradaForm
    template_name = "Posteos/entrada_form.html"
    success_url = reverse_lazy("bienvenida")
    


class EntradaUpdateView(UpdateView):
    model = Entrada
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'creado']
    success_url = reverse_lazy('bienvenida')


class EntradaDeleteView(DeleteView):
    model = Entrada
    success_url = reverse_lazy('bienvenida')

def quienes_somos(request):
    #posteos = Entrada.objects.all()
    return render(request, "quienes_somos.html")