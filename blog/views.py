from rest_framework import viewsets
from .models import Category, Post
from .serializers import CategorySerializer, PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
