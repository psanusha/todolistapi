from django.http import Http404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Category, Task
from api.serializer import CategorySerializer, TaskSerializer
from rest_framework import status

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
            return Response({'message': 'Title updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'error', 'error': serializer.errors})


class CategoryDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'delete']
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except:
            raise Http404
    def delete(self, request, pk, format=None):
        categoryData = self.get_object(pk)
        categoryData.delete()
        return Response({'message': 'success,Category deleted'})

"""
TASK 
"""
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        taskData = Task.objects.all()
        serializer = TaskSerializer(taskData, many=True)
        return Response(serializer.data)

class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        data = request.data
        data['created_by'] = request.user.pk
        existing_task = Task.objects.filter(title=data.get('title', None)).first()
        if existing_task:
            raise ValidationError({'message': 'A task with this title already exists.'})
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )

class TaskDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self,pk):
        try:
            return Task.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request,pk,format=None):
        taskData = self.get_object(pk)
        serializer = TaskSerializer(taskData)
        return Response(serializer.data, status= status.HTTP_200_OK)

class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except:
            raise Http404
    def put(self,request,pk,format=None):
        taskData = self.get_object(pk)
        serializer = TaskSerializer(taskData, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Task updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': 'error', 'error': serializer.errors})


class TaskDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'delete']
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except:
            raise Http404
    def delete(self, request, pk, format=None):
        taskData = self.get_object(pk)
        taskData.delete()
        return Response({'message': 'success,User deleted'})