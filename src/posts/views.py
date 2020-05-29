from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def likePost(request, *args, **kwargs):
    """
    Login user likes/unlikes a post and reponse the new post info
    """
    id = kwargs['id']
    user = request.user
    if request.method == 'POST':
        post = Post.like(id, user)
    else:
        post = Post.unlike(id, user)
    context = {'request': request}
    serializer = PostSerializer(post, context=context)
    return Response(serializer.data)
