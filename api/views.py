from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Category
from api.serializer import CategorySerializer
from rest_framework import generics, status


# Create your views here.
# class Category(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class CategoryUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class CategoryCreate(generics.CreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class CategoryDelete(generics.DestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        data = request.data
        data['created_by'] = request.user.pk
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class CategoryUpdateView(APIView):
    def put(self,request,format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            category = serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)