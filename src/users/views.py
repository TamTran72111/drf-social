from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    get_object_or_404
)

from .serializers import UserRegistrationSerializer, UserSerializer
from .models import User


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer


class UserView(RetrieveAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        username = self.kwargs['username']
        return get_object_or_404(User, username=username)
