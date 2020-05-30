from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.db import models


class User(AbstractUser):
    """
    Create new user model to add features
    """

    def follow(self, user):
        """
        Follow a user if not follow yet

        Args:
            user (User): the following user
        """
        if not self.is_following(user):
            print(self.is_following(user))
            self.following.create(following=user)

    def unfollow(self, user):
        """
        Unfollow a user if is following

        Args:
            user (User): the following user
        """
        if self.is_following(user):
            self.following.filter(following=user).delete()

    def is_following(self, user):
        """
        Check whether `self` is following `user`

        Args:
            user (User): the following user

        Returns:
            True if `user` is `self` or `self` is following `user`.
            False otherwise.
        """
        return bool(
            self == user or
            user.followers.filter(follower=self)
        )

    def like(self, obj):
        """
        Like the obj if it is not already liked

        Args:
            obj: Post or Comment object

        """
        object_id = obj.id
        obj = ContentType.objects.get_for_model(obj)
        if not self.liked(obj):
            self.likes.create(content_type=obj, object_id=object_id)

    def unlike(self, obj):
        """
        Unlike the obj if it is already liked

        Args:
            obj: Post or Comment object

        """
        obj = ContentType.objects.get_for_model(obj)
        if self.liked(obj):
            self.likes.filter(content_type=obj).delete()

    def liked(self, obj):
        """
        Return whether user already liked obj

        Args:
            obj: Post or Comment object (may wrapped by ContentType)

        Returns:
            bool: True if the current user already liked obj. False otherwise.
        """
        object_id = obj.id
        if not isinstance(obj, ContentType):
            obj = ContentType.objects.get_for_model(obj)
        return bool(self.likes.filter(content_type=obj, object_id=object_id))


class Follower(models.Model):
    follower = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
    )

    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='followers',
    )

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.follower.username} is' +\
            f' following {self.following.username}'
