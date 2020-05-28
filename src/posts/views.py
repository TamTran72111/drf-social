from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
