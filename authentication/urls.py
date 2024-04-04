from django.urls import path

from . import views
from .views import UserRegistrationView, UserLoginView, UserLogoutView, UserViewSet

urlpatterns = [
    path('register',UserRegistrationView.as_view(),name='register'),
    path('login',UserLoginView.as_view(),name='login'),
    path('logout',UserLogoutView.as_view(),name='logout'),

    path('userlist',UserViewSet.as_view({'get': 'list'}),name='userList')

]