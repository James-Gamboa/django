from rest_framework import serializers
from .models import Cliente, Pedido, Producto, Empleado, MetodoPago, PedidoProducto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

    def validate_nombre(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El nombre del producto debe tener al menos 3 caracteres.")
        return value

    def validate_descripcion(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("La descripción del producto debe tener al menos 10 caracteres.")
        return value



    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError("El precio del producto debe ser mayor a 0.")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError("El stock del producto no puede ser negativo.")
        return value

#  {
#    "nombre": "Pl",
#    "descripcion": "Consola ",
#    "precio": -1,
#    "stock": -45
#  }

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = '__all__'

    def validate_email(self, value):
        if not "@" in value:
            raise serializers.ValidationError("El email debe ser válido.")
        return value

    def validate_cargo(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El cargo debe tener al menos 3 caracteres.")
        return value

# {
#   "nombre": "",
#   "correo": "mario.com",
#   "telefono": "abc123"
# }

class MetodoPagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPago
        fields = '__all__'

    def validate_tipo(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El tipo de método de pago debe tener al menos 3 caracteres.")
        return value

# {
#   "tipo": "T",
#   "descripcion": ""
# }

class PedidoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoProducto
        fields = '__all__'
