from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken

from kleverApp.models import Videos, FavoriteVideo

from ..serializers import FavoriteVideoSerializer, RegisterSerializer, VideosSerializer


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

