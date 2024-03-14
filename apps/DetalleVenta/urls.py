from django.urls import path
from apps.DetalleVenta.api import detalleVenta_api_view,detalleVenta_detail_api_view

urlpatterns = [
    path('detalleVentas/', detalleVenta_api_view, name='detalleVentas_api'),
    path('detalleVentas/<int:pk>', detalleVenta_detail_api_view, name='detalleVenta_detail_api_view'),
]