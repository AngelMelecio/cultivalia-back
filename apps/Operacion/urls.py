from django.urls import path
from apps.Operacion.api import operacion_api_view,operacion_detail_api_view

urlpatterns = [
    path('operacions/', operacion_api_view, name='operacions_api'),
    path('operacions/<int:pk>', operacion_detail_api_view, name='operacion_detail_api_view'),
]