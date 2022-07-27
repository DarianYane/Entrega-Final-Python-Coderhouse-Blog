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
