from django.forms import DateField, ModelForm
from .models import Entrada
from django import forms

class EntradaForm(ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'
       

class BusquedaEntrada(forms.Form):
    nombre = forms.CharField()
