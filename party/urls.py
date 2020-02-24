
from django.urls import path
from django.conf.urls import include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
=======
    #path('admin/', admin.site.urls),
>>>>>>> 9e007c8d4879154fa94aaaaec53cd6b34a9f382d
    path('api/list', views.get_rest_list, name='get_rest_list'),
]
