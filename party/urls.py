
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/list', views.get_rest_list, name='get_rest_list'),
]
