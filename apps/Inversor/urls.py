from django.urls import path
from apps.Inversor.api import inversor_api_view,inversor_detail_api_view

urlpatterns = [
    path('inversors/', inversor_api_view, name='inversors_api'),
    path('inversors/<int:pk>', inversor_detail_api_view, name='inversor_detail_api_view'),
]