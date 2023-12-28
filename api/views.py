from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Todos, Post, Comment
from .serializers import UserSerializer, TodosSerializer, PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de usuários
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TodosViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados Todos
    """
    queryset = Todos.objects.all()
    serializer_class = TodosSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados de post
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    Permite a manipulação de dados comment
    """
    queryset = Comment.objects.all()
    serializer_class = PostSerializer