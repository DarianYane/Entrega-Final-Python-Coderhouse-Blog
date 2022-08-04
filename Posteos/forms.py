from django.forms import DateField, ModelForm
from .models import Entrada
from django import forms
from .models import Entrada

class EntradaForm(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ('titulo', 'subtitulo', 'cuerpo', 'imagen', 'autor', 'creado') 

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            #'imagen': forms.URLField(attrs={'class': 'form-control'}), ESTE ME DA PROBLEMA
            'autor':  forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id':'elder', 'type': 'hidden'}),
            #'creado':  forms.DateTimeField(attrs={'class': 'form-control'}), ESTE ME DA PROBLEMA

        }    
       

class BusquedaEntrada(forms.Form):
    nombre = forms.CharField()
