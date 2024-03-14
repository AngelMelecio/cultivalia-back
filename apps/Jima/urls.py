from django.urls import path
from apps.Jima.api import jima_api_view,jima_detail_api_view

urlpatterns = [
    path('jimas/', jima_api_view, name='jimas_api'),
    path('jimas/<int:pk>', jima_detail_api_view, name='jima_detail_api_view'),
]