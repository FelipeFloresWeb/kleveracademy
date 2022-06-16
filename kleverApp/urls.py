from django.urls import path
from knox import views as knox_views
from . import views

app_name = 'kleverApp'

urlpatterns = [
    path('user/add', views.add_user, name='add_user'),
    path('user/login', views.login_api, name='login_api'),
    path('user/refresh-login', views.refresh_login, name='refresh-login_api'),
    path('user/logout', knox_views.LogoutView.as_view(), name='logout'),
    path('user/logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/videos', views.get_all_videos, name='get_all_videos'),
    path('user/favorite-videos', views.get_all_user_favorite_videos, name='get_all_user_favorite_videos'),
    path('user/add-favorite-video', views.add_favorite_Video, name='add_favorite_Video'),
    path('user/remove-favorite-video', views.remove_favorite_Video, name='remove_favorite_Video'),
]
