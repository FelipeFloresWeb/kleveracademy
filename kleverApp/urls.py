from django.urls import path
from . import views

app_name = 'kleverApp'

urlpatterns = [
    path('user/', views.getUsers, name='listUsers'),
    path('user/add', views.addUser, name='addUser'),
    path('user/login', views.loginUser, name='loginUser'),
]
