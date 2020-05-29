from rest_framework import serializers


class LikeSerializerMixin(serializers.Serializer):
    """
    Like Serializer Mixin class is used to add likes and is_liked field to
    model that supports `Like` feature.
    """
    likes = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.liked.count()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return user and user.is_authenticated and user.liked(obj)
