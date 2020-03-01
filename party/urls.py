
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import views as auth_v
from users import views as user_v

urlpatterns = [
    #path('', views.index, name='index'),
    #path('admin/', admin.site.urls),
    url('api/list', views.get_rest_list, name="get_rest_list"),
    #path('', include("main.urls")),
    #path('', include("django.contrib.auth.urls")),
    url('admin/', admin.site.urls),
    url('register/'', user_v.register, name='register'),
    url('login/', auth_v.LoginView.as_view(), name='login'),
    url('logout/', auth_v.LogoutView.as_view(), name='logout'),
    url('', include('party.urls')),
    path('party/new/', views.party_new, name='party_new'),
    path('party/<int:pk>/edit/', views.party_edit, name='party_edit'),
    path('party/<int:pk>/', views.party_detail, name='party_detail'),
]
