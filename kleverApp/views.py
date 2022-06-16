from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

from kleverApp.models import Videos, FavoriteVideo

from .serializers import FavoriteVideoSerializer, RegisterSerializer, VideosSerializer


@api_view(['POST'])
def add_user(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        _, token = AuthToken.objects.create(user)
        return Response({
            'userInfo': {
                'firstName': user.first_name,
                'lastName': user.last_name,
                'email': user.email,
            },
            'token': token
        }, status=201)


@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.validated_data['user']

        _, token = AuthToken.objects.create(user)
        return Response({
            'userInfo': {
                'firstName': user.first_name,
                'lastName': user.last_name,
                'email': user.email,
            },
            'token': token
        }, status=200)


@api_view(['POST'])
def refresh_login(request):
    user = request.user

    if(user.is_authenticated):
        _, token = AuthToken.objects.create(user)

        return Response({
            'userInfo': {
                'firstName': user.first_name,
                'lastName': user.last_name,
                'email': user.email,
            },
            'token': token
        }, status=200)

    return Response({
        'message': 'You are not authenticated'
    }, status=401)

@api_view(['POST'])
def get_all_videos(request):
    videos = Videos.objects.all()
    serializer = VideosSerializer(videos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def get_all_user_favorite_videos(request):
    user = request.user

    if(user.is_authenticated):
        favorite_videos = FavoriteVideo.objects.filter(user=user)

        ids = [video.video.id for video in favorite_videos]

        videos = Videos.objects.filter(id__in=ids)
        serializervideo = VideosSerializer(videos, many=True)

        return Response(serializervideo.data, status=200)


    return Response({
        'message': 'You are not authenticated'
    }, status=401)


@api_view(['POST'])
def add_favorite_Video(request):
    user = request.user

    if(user.is_authenticated):
        video_id = request.data['video_id']
        video = Videos.objects.get(id=video_id)

        favorite_video = FavoriteVideo.objects.create(user=user, video=video)
        serializer = FavoriteVideoSerializer(favorite_video)
        if serializer.is_valid(raise_exception=True):
            return Response({"Status": "ok", "videoAdded": serializer.data}, status=201)

    return Response({
        'message': 'You are not authenticated'
    }, status=401)


@api_view(['DELETE'])
def remove_favorite_Video(request):
    user = request.user

    if(user.is_authenticated):
        video_id = request.data['video_id']
        video = Videos.objects.get(id=video_id)

        favorite_video = FavoriteVideo.objects.get(user=user, video=video)
        favorite_video.delete()

        return Response({"Status": "ok", "videoRemoved": video_id}, status=200)

