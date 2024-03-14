from django.urls import path
from apps.Asesor.api import asesor_api_view,asesor_detail_api_view

urlpatterns = [
    path('asesors/', asesor_api_view, name='asesors_api'),
    path('asesors/<int:pk>', asesor_detail_api_view, name='asesor_detail_api_view'),
]