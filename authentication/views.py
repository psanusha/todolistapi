from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from rest_framework import generics, permissions, status, viewsets
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from authentication.serializer import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from rest_framework.response import Response


# Create your views here.
class UserRegistrationView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.create(serializer.data)
            return Response({"status": "success", "code": status.HTTP_201_CREATED, "details": serializer.data})
        return Response({"status": "unsuccessful", "code": status.HTTP_400_BAD_REQUEST, "details": serializer.errors})


class UserLoginView(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        print(request.data)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        print(user)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)


class UserLogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
            try:
                # Delete the user's token to logout
                request.user.auth_token.delete()
                return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


##------------------ADMIN SIDE--------------------------##
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes([IsAdminUser])


