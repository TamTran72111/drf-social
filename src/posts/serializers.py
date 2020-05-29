from rest_framework import serializers

from likes.serializers import LikeSerializerMixin
from .models import Post


class PostSerializer(LikeSerializerMixin, serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'post', 'created_on', 'likes', 'is_liked']

    def save(self, **kwargs):
        """
        Update author information based on request before saving
        """
        self._validated_data['author'] = self.context['request'].user
        return super().save(**kwargs)
