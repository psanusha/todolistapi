from django.urls import path
from api.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDetailsView, CategoryDeleteView, \
    TaskListView, TaskCreateView, TaskDetailsView, TaskDeleteView, TaskUpdateView

urlpatterns = [
    path('categorylist/',CategoryListView.as_view(),name='categorylist'),
    path('categorycreate/',CategoryCreateView.as_view(),name='categorycreate'),
    path('categorydetails/<int:pk>/',CategoryDetailsView.as_view(),name='categoryupdate'),
    path('categoryupdate/<int:pk>/', CategoryUpdateView.as_view(),name='categoryupdate'),
    path('categorydelete/<int:pk>/', CategoryDeleteView.as_view(),name='categorydelete'),

    path('tasklist/',TaskListView.as_view(),name='tasklist'),
    path('taskcreate/',TaskCreateView.as_view(),name='taskcreate'),
    path('taskdetails/<int:pk>/', TaskDetailsView.as_view(),name='taskdetails'),
    path('taskupdate/<int:pk>/', TaskUpdateView.as_view(),name='taskupdate'),
    path('taskdelete/<int:pk>/', TaskDeleteView.as_view(),name='taskdelete'),



]