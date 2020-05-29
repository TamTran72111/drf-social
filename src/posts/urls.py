from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewset, likePost

router = DefaultRouter()
router.register('', PostViewset)

urlpatterns = [
    path('like/<int:id>/', likePost, name='post-like'),
    path('', include(router.urls)),
]
