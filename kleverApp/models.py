from django.db import models


class Videos(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    rate = models.FloatField(default=0)
    rate_length = models.IntegerField(default=0)
    rate_calc = models.FloatField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class FavoriteVideo(models.Model):
    user = models.ForeignKey('auth.User', related_name='favorite_videos', on_delete=models.CASCADE)
    video = models.ForeignKey(Videos,  related_name='favorite_videos', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username + ' - ' + self.video.title


