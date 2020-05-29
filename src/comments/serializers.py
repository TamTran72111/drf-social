from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from posts.models import Post
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['username', 'comment', 'created_on']

    def save(self, **kwargs):
        """
        Update author information based on request before saving
        """
        self._validated_data['post'] = get_object_or_404(
            Post,
            id=self.context['view'].kwargs['post_id'],
        )
        self._validated_data['author'] = self.context['request'].user
        return super().save(**kwargs)
