from rest_framework.viewsets import ModelViewSet

from posts.permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer
from .models import Comment


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]
