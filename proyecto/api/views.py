from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets # type: ignore
from .models import Cliente, Pedido, Producto, Empleado, MetodoPago, PedidoProducto
from .serializers import ClienteSerializer, PedidoSerializer, ProductoSerializer, EmpleadoSerializer, MetodoPagoSerializer, PedidoProductoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer

class MetodoPagoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPago.objects.all()
    serializer_class = MetodoPagoSerializer

class PedidoProductoViewSet(viewsets.ModelViewSet):
    queryset = PedidoProducto.objects.all()
    serializer_class = PedidoProductoSerializer
