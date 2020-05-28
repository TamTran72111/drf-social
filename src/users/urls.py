from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from .views import UserRegistrationView, UserView

urlpatterns = [
    path('register', UserRegistrationView.as_view(), name='user-register'),
    path('login', TokenObtainPairView.as_view(), name='user-login'),
    path('refresh-token', TokenRefreshView.as_view(), name='refresh-token'),
    path('users/<str:username>', UserView.as_view(), name='user-detail')
]
