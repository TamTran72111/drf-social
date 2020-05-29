from django.db import models

from posts.models import Post
from users.models import User


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} commented on post {} at {}'.format(
            self.author.username,
            self.post.id,
            self.created_on
        )
