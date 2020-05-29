from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from likes.models import Like, LikeMixin
from users.models import User


class Post(models.Model, LikeMixin):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    post = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    liked = GenericRelation(Like)

    def __str__(self):
        return f'{self.author.username} posted on {self.created_on}'
