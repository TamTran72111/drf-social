from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType


class User(AbstractUser):
    """
    Create new user model to add features
    """

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
        if not isinstance(obj, ContentType):
            obj = ContentType.objects.get_for_model(obj)
        return self.likes.filter(content_type=obj).count() > 0
