from django.urls import path
from apps.Administrador.api import administrador_api_view,administrador_detail_api_view

urlpatterns = [
    path('administradors/', administrador_api_view, name='administradors_api'),
    path('administradors/<int:pk>', administrador_detail_api_view, name='administrador_detail_api_view'),
]