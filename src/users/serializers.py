from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password',
                  'last_name', 'first_name', 'access', 'refresh']
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }

    def save(self, **kwargs):
        user = super().save(**kwargs)
        user.set_password(user.password)
        user.save()
        refresh = RefreshToken.for_user(user)
        user.refresh = str(refresh)
        user.access = str(refresh.access_token)
        return user
