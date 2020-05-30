from rest_framework import serializers

from posts.serializers import PostSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    is_following = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['username', 'is_following', 'followers', 'posts']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['posts'] = PostSerializer(
            many=True,
            read_only=True,
            context=self.context
        )

    def get_is_following(self, user):
        current_user = self.context['request'].user
        return bool(
            current_user and 
            current_user.is_authenticated and 
            current_user.is_following(user)
        )

    def get_followers(self, user):
        return user.followers.count()