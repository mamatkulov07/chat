from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=40, unique=True)


class Chat(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User, related_name='chats')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='chat_image/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    image = models.ImageField(upload_to='message_image/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    last_activity = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chat











