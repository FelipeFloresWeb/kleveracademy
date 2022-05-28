from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password


@api_view(['GET'])
def getUsers():
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
    request.data['password'] = make_password(request.data['password'])

    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def loginUser(request):
    email = request.data['email']
    password = request.data['password']

    if email and password:
        try:
            user = User.objects.get(email=email, password=password)
            if(user):
                return Response(data={'message': 'User successfully found.'}, status=200)
        except User.DoesNotExist:
            return Response(data={'message': 'User not found.'}, status=404)

    else:
        return Response(
            data={'message': 'The fileds email and password are required'},
            status=400,
        )
