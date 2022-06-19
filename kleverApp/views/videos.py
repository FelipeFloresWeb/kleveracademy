from rest_framework.decorators import api_view
from kleverApp.models import RateVideo, Videos, FavoriteVideo
from kleverApp.serializers import FavoriteVideoSerializer, VideosSerializer
from rest_framework.response import Response


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
        exists = FavoriteVideo.objects.filter(user=user, video=video).exists()
        if not exists:
            favorite_video = FavoriteVideo(user=user, video=video)
            favorite_video.save()
            return Response({
                'message': 'Video added to favorites'
            }, status=200)
        else:
            return Response({
                'message': 'Video already in favorites'
            }, status=200)
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


@api_view(['POST'])
def add_video_rate(request):
    user = request.user

    if(user.is_authenticated):
        video_id = request.data['video_id']
        rate = request.data['rate']
        video = Videos.objects.get(id=video_id)
        exists = RateVideo.objects.filter(user=user, video=video).exists()
        if not exists:
            video_rate_length = RateVideo.objects.filter(video=video).count()
            video.rate = (video.rate + rate) / (video_rate_length + 1)
            rate_video = RateVideo(user=user, video=video, rate=rate)
            rate_video.save()
            video.save()
            return Response({
                'message': 'Video rate added'
            }, status=200)
        else:
            return Response({
                'message': 'Video rate already added'
            }, status=409)

    return Response({
        'message': 'You are not authenticated'
    }, status=401)
