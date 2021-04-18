from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from polls.models import Paper, Comment, Login
from polls.serializer import PaperSerializer, CommentSerializer, LoginSerializer



class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer