from django.contrib.auth.models import User
from rest_framework import serializers, validators
from django.contrib.auth.hashers import make_password

from kleverApp.models import Article, Videos, FavoriteVideo


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}, 'email': {
            'required': True, 'validators': [validators.UniqueValidator(queryset=User.objects.all())], 'allow_blank': False}}

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = make_password(
            validated_data['password'], salt=None, hasher='default')
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        user = User.objects.create(username=username, email=email,
                                   password=password, first_name=first_name, last_name=last_name)
        return user

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Videos
        fields = ('id','title', 'description', 'video_url', 'thumbnail_url', 'isFeatured', 'published_at', 'rate', 'likes', 'created_at', 'updated_at')

class FavoriteVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteVideo
        fields = ('user', 'video')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'text', 'font', 'published_at', 'read_time', 'description', 'thumbnail_url', 'isFeatured', 'created_at', 'updated_at')