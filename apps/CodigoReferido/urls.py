from django.urls import path
from apps.CodigoReferido.api import codigoReferido_api_view,codigoReferido_detail_api_view

urlpatterns = [
    path('codigoReferidos/', codigoReferido_api_view, name='codigoReferidos_api'),
    path('codigoReferidos/<int:pk>', codigoReferido_detail_api_view, name='codigoReferido_detail_api_view'),
]