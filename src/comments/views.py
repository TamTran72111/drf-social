from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer
from .models import Comment


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post__id=post_id)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def likeComment(request, *args, **kwargs):
    """
    Login user likes/unlikes a comment and reponse the new comment info
    """
    id = kwargs['id']
    user = request.user
    if request.method == 'POST':
        comment = Comment.like(id, user)
    else:
        comment = Comment.unlike(id, user)
    serializer = CommentSerializer(comment)
    return Response(serializer.data)
