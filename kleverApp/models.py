# from django.db import models


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(max_length=255, unique=True)
#     password = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.email


# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     views = models.IntegerField(default=0)
#     likes = models.IntegerField(default=0)
#     description = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
