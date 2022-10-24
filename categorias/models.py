from django.db import models

# Create your models here.
class Categorias(models.Model):
    titulo = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length = 100)
    fecha_creacion = models.DateField(auto_created=True)
    fecha_modificacion = models.DateField(auto_now=True)

    def __str___(self):
        return self.title