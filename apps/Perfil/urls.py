from django.urls import path
from apps.Perfil.api import perfil_api_view,perfil_detail_api_view

urlpatterns = [
    path('perfils/', perfil_api_view, name='perfils_api'),
    path('perfils/<int:pk>', perfil_detail_api_view, name='perfil_detail_api_view'),
]