from django.urls import path
from apps.Usuario.api import usuario_api_view,usuario_detail_api_view

urlpatterns = [
    path('usuarios/', usuario_api_view, name='usuarios_api'),
    path('usuarios/<int:pk>', usuario_detail_api_view, name='usuario_detail_api_view'),
]