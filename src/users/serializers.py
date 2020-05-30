from rest_framework import serializers

from posts.serializers import PostSerializer
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'posts']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['posts'] = PostSerializer(
            many=True,
            read_only=True,
            context=self.context
        )
        print("--------------------------")
        print(self.context.keys())
        print("--------------------------")
