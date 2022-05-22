from django.urls import path
from . import views

app_name = 'kleverApp'

urlpatterns = [
    path('user/', views.getUsers, name='listUsers'),
    path('user/<slug:slug>', views.getUser, name='listUser'),
    path('user/add', views.addUser, name='addUser'),
    # path('user/<slug:slug>/', views.UserDetailView.as_view(), name='detail'),
]
