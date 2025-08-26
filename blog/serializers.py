from rest_framework import serializers
from .models import Category, Post

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        model = Post
        fields = ["id", "title", "content", "created_at", "category", "category_id"]
