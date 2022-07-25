from django.db import models
from datetime import datetime, date, time
from ckeditor.fields import RichTextField

# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = RichTextField()
    imagen = models.URLField()
    # imagen = models.models.ImageField(upload_to="articles", null = True, blank = True)
    autor = models.CharField(max_length=50)
    creado = models.DateField(default=date.today()) #(15 Julio 2022)  # (auto_now_add=True) o (auto_now=True)

    class Meta:
        ordering = ['-creado'] #Ordena los post de más nuevos a más viejos

    def __str__(self):
        return self.titulo
    
     