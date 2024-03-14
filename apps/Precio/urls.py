from django.urls import path
from apps.Precio.api import precio_api_view,precio_detail_api_view

urlpatterns = [
    path('precios/', precio_api_view, name='precios_api'),
    path('precios/<int:pk>', precio_detail_api_view, name='precio_detail_api_view'),
]