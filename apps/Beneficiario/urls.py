from django.urls import path
from apps.Beneficiario.api import beneficiario_api_view,beneficiario_detail_api_view

urlpatterns = [
    path('beneficiarios/', beneficiario_api_view, name='beneficiarios_api'),
    path('beneficiarios/<int:pk>', beneficiario_detail_api_view, name='beneficiario_detail_api_view'),
]