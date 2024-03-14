from django.urls import path
from apps.Contrato.api import contrato_api_view,contrato_detail_api_view

urlpatterns = [
    path('contratos/', contrato_api_view, name='contratos_api'),
    path('contratos/<int:pk>', contrato_detail_api_view, name='contrato_detail_api_view'),
]