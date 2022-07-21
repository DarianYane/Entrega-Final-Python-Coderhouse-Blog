from django.forms import ModelForm
from .models import Entrada

class EntradaForm(ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'