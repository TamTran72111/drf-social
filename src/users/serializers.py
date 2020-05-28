from rest_framework import serializers

from posts.serializers import PostSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['username', 'posts']
