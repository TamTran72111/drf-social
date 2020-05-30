from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import (
    RetrieveAPIView,
    get_object_or_404
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer
from .models import User


class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        username = self.kwargs['username']
        return get_object_or_404(User, username=username)


@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def followView(request, *args, **kwargs):
    """
    Login user follows/unfollows another user
    """
    username = kwargs['username']
    following = get_object_or_404(User, username=username)
    follower = request.user
    if request.method == 'POST':
        follower.follow(following)
    else:
        follower.unfollow(following)
    context = {'request': request}
    serializer = UserSerializer(following, context=context)
    return Response(serializer.data)
