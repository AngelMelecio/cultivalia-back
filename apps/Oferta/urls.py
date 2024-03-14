from django.urls import path
from apps.Oferta.api import oferta_api_view,oferta_detail_api_view

urlpatterns = [
    path('ofertas/', oferta_api_view, name='ofertas_api'),
    path('ofertas/<int:pk>', oferta_detail_api_view, name='oferta_detail_api_view'),
]