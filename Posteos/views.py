from msilib.schema import ListView
from typing import List
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from Posteos.models import Entrada
from Posteos.forms import EntradaForm, BusquedaEntrada
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

#Eliminar este de testeos antes de entregar el trabajo
def test(request):
    #posteos = Entrada.objects.all()
    return render(request, "test.html") #{'posteos': posteos}



def home(request):
    posteos = Entrada.objects.all()
    return render(request, "bienvenida.html", {'posteos': posteos})

def crearPost(request):
    form = EntradaForm()
    
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenida')

    context ={'form': form}
    return render(request, "crearpost.html", context)


def buscar(request):
    if request.GET["titulo"]:
        queryset = request.GET["titulo"]       
        entradas = Entrada.objects.filter(titulo__icontains=queryset).all()
        #print(queryset)
        #print(entradas)

        if entradas!=[]:
            return render(request, "busqueda_entrada.html", {"entradas": entradas, "titulo": queryset})


    else:
        queryset = "(No realizó búsqueda)"
        return render(request, "busqueda_entrada.html", {"titulo": queryset})
    
    
def eliminarPost(request,id):
    post = get_object_or_404(Entrada, id=id)
    #print(post)

    #eliminamos el registro
    post.delete()

    #redirecciono a la ruta raiz
    return redirect('/')

# Clases basadas en vistas
class EntradaList(ListView):

    model = Entrada
    template_name: "bienvenida.html"

class EntradaDetalle(DetailView):

    model = Entrada
    template_name: "detalle_entrada.html"

class EntradaCreacion(CreateView):

    model = Entrada
    succes_url = "bienvenida.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'creado']

class EntradaUpdate(UpdateView):

    model = Entrada
    succes_url = "bienvenida.html"
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'creado']

class EntradaDelete(DeleteView):

    model = Entrada
    succes_url = "bienvenida.html"
    
def editarPost(request,id):
    print(id)
    if request.method == 'GET':
        post = get_object_or_404(Entrada, id=id)
        print(post)
        initial = {'titulo':Entrada.titulo, 'subtitulo':Entrada.subtitulo, 
        'cuerpo':Entrada.cuerpo, 'imagen':Entrada.imagen, 'autor':Entrada.autor, 'creado':Entrada.creado}
        print(initial)
        form = EntradaForm(initial=initial)
        print(form)
        return render(request, "crearpost.html", {'form':form})


    """
    print(id)
    post = Entrada.objects.get(id=id)
    print(post)
    

    if request.method == 'POST':
        form = EntradaForm(request.POST)
        print(form)

        if form.is_valid():
            
            informacion = form.cleaned_data
            print(informacion)

        
                Entrada.titulo = informacion['titulo']
                Entrada.subtitulo = informacion['subtitulo']
                Entrada.cuerpo = informacion['cuerpo']
                Entrada.imagen = informacion['imagen']
                Entrada.autor = informacion['autor']
                Entrada.creado = informacion['creado']


                form.save()
                return redirect('bienvenida')

        context ={'form': form}
        return render(request, "crearpost.html", context)
        
    else:
        # Creo el formulario con los datos a modificar
        form = EntradaForm(initial={'titulo':Entrada.titulo, 'subtitulo':Entrada.subtitulo, 
        'cuerpo':Entrada.cuerpo, 'imagen':Entrada.imagen, 'autor':Entrada.autor, 'creado':Entrada.creado})
        print(form)
        print(1)
        
    #redirecciono a la r
    context ={'form': form}
    return render(request, "crearpost.html", context)
    """
