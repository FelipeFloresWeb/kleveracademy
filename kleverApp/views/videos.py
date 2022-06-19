from rest_framework.decorators import api_view
from kleverApp.models import Videos, FavoriteVideo
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


@api_view(['POST'])
def add_video_rate(request):
    user = request.user

    if(user.is_authenticated):
        video_id = request.data['video_id']
        rate = request.data['rate']
        video = Videos.objects.get(id=video_id)

        video.rate_length += 1
        video.rate = video.rate + rate
        calc = format(video.rate / video.rate_length, '.2f')
        video.rate_calc = calc

        print(f"video.rate_length: {video.rate_length}\nvideo.rate: {calc}")
        video.save()

        return Response({"Status": "ok", "videoRated": video_id, "newRate": calc }, status=200)

    return Response({
        'message': 'You are not authenticated'
    }, status=401)