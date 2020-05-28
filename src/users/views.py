from rest_framework.generics import (
    RetrieveAPIView,
    get_object_or_404
)

from .serializers import UserSerializer
from .models import User


class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        username = self.kwargs['username']
        return get_object_or_404(User, username=username)
