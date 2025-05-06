from django.urls import include, path # type: ignore
from rest_framework.routers import DefaultRouter # type: ignore
from .views import ClienteViewSet, PedidoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
