from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Entrada(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=100)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to="Posteos/images/")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    creado = models.DateTimeField(default=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    class Meta:
        ordering = ['-creado'] #Ordena los post de más nuevos a más viejos
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.titulo +" - (Creada por: "+ str(self.autor)+")"

