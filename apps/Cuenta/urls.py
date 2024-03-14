from django.urls import path
from apps.Cuenta.api import cuenta_api_view,cuenta_detail_api_view

urlpatterns = [
    path('cuentas/', cuenta_api_view, name='cuentas_api'),
    path('cuentas/<int:pk>', cuenta_detail_api_view, name='cuenta_detail_api_view'),
]