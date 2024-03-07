from django.http import Http404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Category
from api.serializer import CategorySerializer
from rest_framework import generics, status

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

class CategoryDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request,pk,format=None):
        categoryData = self.get_object(pk)
        serializer = CategorySerializer(categoryData)
        return Response(serializer.data, status= status.HTTP_200_OK)

class CategoryUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Http404
    def put(self,request,pk,format=None):
        categoryData = self.get_object(pk)
        serializer = CategorySerializer(categoryData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'message': 'error', 'error': serializer.errors})


