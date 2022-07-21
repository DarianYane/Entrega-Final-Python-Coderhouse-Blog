from django.shortcuts import render, redirect
from Posteos.models import Entrada
from Posteos.forms import EntradaForm

# Create your views here.
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