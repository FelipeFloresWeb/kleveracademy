from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# def getUserById(request):
#     try:
#         user = User.objects.get(request.GET.get('id'))
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#     except User.DoesNotExist:
#         return Response(status=404, data={'error': 'User not found'})


@api_view(['POST'])
def addUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def editUser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
