from django.urls import path
from .views import *


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('userprofile/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='userprofile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='userprofile_detail'),

    path('chat/', ChatViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='chat_list'),
    path('chat/<int:pk>/', ChatViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='chat_detail'),

    path('message/', MessageViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='message_list'),
    path('Message/<int:pk>/', MessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='message_detail'),

]