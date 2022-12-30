from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

from rest_framework import generics, status
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import SignUpSerializer, GetUserSerializer, SignUpAdminSerializer
from .tokens import create_jwt_pair_for_user
from .models import User

# Create your views here.

class SignUpView(generics.GenericAPIView):
  serializer_class = SignUpSerializer

  def post(self, request: Request):
    data = request.data
    serializer = self.serializer_class(data=data)
    if serializer.is_valid():
      
      serializer.save()
      
      response = {"message": "El usuario se creó correctamente", "data": serializer.data}
  
      return Response(data=response, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignUpAdminView(generics.GenericAPIView):
  serializer_class = SignUpAdminSerializer

  def post(self, request: Request):
    data = request.data
    serializer = self.serializer_class(data=data)

    if serializer.is_valid():
      serializer.save()
      response = {"message": "El super usuario se creó correctamente", "data": serializer.data}
  
      return Response(data=response, status=status.HTTP_201_CREATED)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

  def post(self, request: Request):
    email = request.data.get("email")
    password = request.data.get("password")

    user = authenticate(email=email, password=password)
    if user is not None:
      tokens = create_jwt_pair_for_user(user)
      idUser = User.objects.get(email=email)
      user_data = {
        'id': idUser.id,
        'username':idUser.username,
        'email':idUser.email,
        'is_superuser': idUser.is_superuser
      }
      print(user_data)
      response = {"message": "Logeado correctamente", "user_data": user_data ,"tokens": tokens}

      return Response(data=response, status=status.HTTP_200_OK)

    else:
      return Response(data={"message": "Correo inválido o contraseña incorrecta"})

  def get(self, request: Request):
      content = {"user": str(request.user), "auth": str(request.auth)}

      return Response(data=content, status=status.HTTP_200_OK)

class GetUsers(viewsets.ReadOnlyModelViewSet):
  serializer_class = GetUserSerializer
  queryset = User.objects.all()
