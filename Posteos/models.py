from django.db import models
from datetime import datetime, date, time

# Create your models here.
class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField(max_length=4000)
    imagen = models.URLField()
    autor = models.CharField(max_length=50)
    creado = models.DateField(default=date.today()) #(15 Julio 2022)

    class Meta:
        ordering = ['-creado'] #Ordena los post de más nuevos a más viejos

    def __str__(self):
        return self.titulo
    
     