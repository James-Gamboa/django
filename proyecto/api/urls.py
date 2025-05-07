from django.urls import include, path 
from rest_framework.routers import DefaultRouter # type: ignore
from .views import ClienteViewSet, PedidoViewSet, ProductoViewSet, EmpleadoViewSet, MetodoPagoViewSet, PedidoProductoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'metodos-pago', MetodoPagoViewSet)
router.register(r'pedidos-productos', PedidoProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
