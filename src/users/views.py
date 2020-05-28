from rest_framework.generics import CreateAPIView
from .serializers import UserRegistrationSerializer
from .models import User


class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
