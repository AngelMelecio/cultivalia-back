from django.urls import path
from apps.Predio.api import predio_api_view,predio_detail_api_view

urlpatterns = [
    path('predios/', predio_api_view, name='predios_api'),
    path('predios/<int:pk>', predio_detail_api_view, name='predio_detail_api_view'),
]