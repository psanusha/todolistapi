from django.urls import path
from api.views import Category, CategoryListView, CategoryCreateView, CategoryUpdateView

urlpatterns = [
    path('categorylist/',CategoryListView.as_view(),name='categorylist'),
    path('categorycreate/',CategoryCreateView.as_view(),name='categorycreate'),
    path('categoryupdate/<int:pk>/', CategoryUpdateView.as_view(),name='categoryupdate'),


]