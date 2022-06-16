from django.db import models


class Videos(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_url = models.CharField(max_length=200)
    thumbnail_url = models.CharField(max_length=200)
    rate = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


