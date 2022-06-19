from django.contrib import admin
from .models import RateVideo, Videos, FavoriteVideo


@admin.register(Videos)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'video_url', 'thumbnail_url', 'likes', 'rate', 'created_at', 'updated_at')

@admin.register(FavoriteVideo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'id')

@admin.register(RateVideo)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'rate')