from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from authentication.serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.response import Response


# Create your views here.
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({"status": "sucess", "code": status.HTTP_201_CREATED, "details": serializer.data})
        return Response({"status": "unsuccessful", "code": status.HTTP_400_BAD_REQUEST, "detsils": serializer.errors})


class UserLoginView(APIView):
    def post(self, request):
        print(request.data)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(user)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)