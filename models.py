from django.db import models



class Autor (models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True,null=True)
   
    def __str__(self):
        return self.nombre


class Libros(models.Model):
    titulo = models.CharField(max_length=100)
    autor=models.ForeignKey(Autor,on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    disponible= models.BooleanField(default=True)

    def __str__(self):
        return self.titulo