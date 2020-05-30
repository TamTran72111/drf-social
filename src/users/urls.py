from django.urls import path

from .views import UserView, followView

urlpatterns = [
    path('<str:username>', UserView.as_view(), name='user-detail'),
    path('<str:username>/follow/', followView, name='follow-user'),
]
