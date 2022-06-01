from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import RegisterSerializer


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

# example of how to use the authentication_classes and permission_classes
# @api_view(['POST'])
# def example_view(request, ):
#     user = request.user

#     if(user.is_authenticated):
#         return Response({
#             'userInfo': {
#                 'username': user.username,
#                 'email': user.email,
#                 'id': user.id,
#             }}, status=200)

#     return Response({
#         'message': 'You are not authenticated'
#     }, status=401)
# Authorization: Token c7d58197d1f6bc6978218e33bcbcceaf632da436521b05b63d725ea7b01c2371
