from django.http import HttpResponse
from django.shortcuts import render, redirect
from Posteos.models import Entrada
from Posteos.forms import EntradaForm, BusquedaEntrada
from django.http import HttpResponse

# Create your views here.

#Eliminar este de testeos antes de entregar el trabajo
def test(request):
    #posteos = Entrada.objects.all()
    return render(request, "navbar.html") #{'posteos': posteos}



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

        if entradas!=[]:
            return render(request, "busqueda_entrada.html", {"entradas": entradas, "titulo": queryset})
        else:
            return redirect('bienvenida')
    else:
        respuesta = "Ha habido un error. Intente nuevamente."
        return render(request, "busqueda_entrada.html", {"respuesta": respuesta})
    
    
    