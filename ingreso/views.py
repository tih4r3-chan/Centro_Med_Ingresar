from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Users
from .serializer import UsersSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (AllowAny,)
    def perform_create(self, serializer):
        user = serializer.save()
        login(self.request, user)

class UserLoginView(generics.CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = (AllowAny,)
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            serializer = self.serializer_class(user)
            return Response(serializer.data)
        else:
            return Response({"error": "Credenciales invalidas"})
        

@api_view(['GET'])
def UsuariosLista(request):
    users = Users.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def CrearUsuarios(request):
    serializer = UsersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def EliminarUsuarios(request, pk):
    user = get_object_or_404(Users, id=pk)
    user.delete()
    return Response('Usuario eliminado')
