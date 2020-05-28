from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'username', 'content', 'created_on']

    def save(self, **kwargs):
        """
        Update author inform base on request.user before save
        """
        self._validated_data['author'] = self.context['request'].user
        return super().save(**kwargs)
