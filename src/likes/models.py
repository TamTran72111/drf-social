from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from rest_framework.generics import get_object_or_404

from users.models import User


class Like(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='likes',
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f'{self.author.username} liked {self.content_type}'


class LikeMixin:
    """
    Support like and unlike behavior
    """

    @classmethod
    def like(cls, id, user):
        """
        User likes an exist object. If the object does not exist,
        raise Http404 exception.

        Args:
            cls  (class): Class using this features
            id   (int)  : id of the target object
            user (User) : the current logging user

        Returns:
            Return target object
        """
        obj = get_object_or_404(cls, id=id)
        user.like(obj)
        return obj

    @classmethod
    def unlike(cls, id, user):
        """
        User unlikes an exist object. If the object does not exist,
        raise Http404 exception.

        Args:
            cls  (class): Class using this features
            id   (int)  : id of the target object
            user (User) : the current logging user

        Returns:
            Return target object
        """
        obj = get_object_or_404(cls, id=id)
        user.unlike(obj)
        return obj
