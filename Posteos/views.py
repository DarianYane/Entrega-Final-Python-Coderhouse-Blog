from django.http import HttpResponse
from django.shortcuts import render, redirect
from Posteos.models import Entrada
from Posteos.forms import EntradaForm, BusquedaEntrada
from django.http import HttpResponse

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
    
    
def eliminarEntrada (request, Entrada_titulo):
    posteo = Entrada.objects.get(titulo=Entrada_titulo)
    posteo.delete()

    #vuelvo al menú
    posteos = Entrada.objects.all()
    return render(request, "bienvenida.html", {'posteos': posteos})