from django.db import models # type: ignore

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, related_name='pedidos', on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_pedido = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Pedido {self.id} de {self.cliente.nombre}"