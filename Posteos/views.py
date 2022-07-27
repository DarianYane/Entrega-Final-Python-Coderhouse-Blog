from django.shortcuts import get_object_or_404, render, redirect
from Posteos.models import Entrada
from Posteos.forms import EntradaForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#Eliminar este de testeos antes de entregar el trabajo
def test(request):
    #posteos = Entrada.objects.all()
    return render(request, "entrada_detail.html") #{'posteos': posteos}



def buscar(request):
    if request.GET["titulo"]:
        queryset = request.GET["titulo"]       
        entradas = Entrada.objects.filter(titulo__icontains=queryset).all()

        if entradas!=[]:
            return render(request, "busqueda_entrada.html", {"entradas": entradas, "titulo": queryset})

    else:
        queryset = "(No realizó búsqueda)"
        return render(request, "busqueda_entrada.html", {"titulo": queryset})
    
    

def eliminarPost(request,id):
    post = get_object_or_404(Entrada, id=id)
    post.delete()

    #redirecciono a la ruta raiz
    return redirect('/')



# No funciona!!!!
def editarPost(request,id):
    
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        print(form)
        
        if form.is_valid():
            
            informacion = form.cleaned_data
                    
            #Entrada.id = informacion['id']
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
        print(id)
        if request.method == 'GET':
            post = get_object_or_404(Entrada, id=id)
            print(post)
            initial = {'id': post.id, 'titulo':post.titulo, 'subtitulo':post.subtitulo, 
            'cuerpo':post.cuerpo, 'imagen':post.imagen, 'autor':post.autor} 
            print(initial)
            form = EntradaForm(initial=initial)
            #print(form)
            return render(request, "crearpost.html", {'form':form})
 
        
    #redirecciono a la r
    context ={'form': form}
    return render(request, "crearpost.html", context)
    

                #CBV

# Funciona
class BienvenidaView(ListView):
    queryset = Entrada.objects.all()
    context_object_name = "posteos"
    template_name = "bienvenida.html"



# Funciona
class EntradaDetailView(DetailView):
    model = Entrada
    context_object_name = "post"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['portal'] = Portal.objects.order_by('date_updated').first()
        return context

# Funciona
class EntradaCreateView(CreateView):
    model = Entrada
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'creado']
    template_name = "Posteos/entrada_form.html"
    success_url = reverse_lazy("bienvenida")

# Funciona
class EntradaUpdateView(UpdateView):
    model = Entrada
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'creado']
    success_url = reverse_lazy('bienvenida')




# no lo probé
class EntradaDelete(DeleteView):

    model = Entrada
    succes_url = "bienvenida.html"



#Clases del profesor
    
"""
class ArticleDeleteView(BaseView, DeleteView):
    model = Entrada
    success_url = reverse_lazy('panel-page')
"""