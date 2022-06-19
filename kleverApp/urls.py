from django.urls import path
from knox import views as knox_views
from .views import views, videos

app_name = 'kleverApp'

urlpatterns = [
    path('user/add', views.add_user, name='add_user'),
    path('user/login', views.login_api, name='login_api'),
    path('user/refresh-login', views.refresh_login, name='refresh-login_api'),
    path('user/logout', knox_views.LogoutView.as_view(), name='logout'),
    path('user/logoutall', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/videos', videos.get_all_videos, name='get_all_videos'),
    path('user/favorite-videos', videos.get_all_user_favorite_videos, name='get_all_user_favorite_videos'),
    path('user/add-favorite-video', videos.add_favorite_Video, name='add_favorite_Video'),
    path('user/remove-favorite-video', videos.remove_favorite_Video, name='remove_favorite_Video'),
    path('user/add-video-rate', videos.add_video_rate, name='add_video_rate'),
]
