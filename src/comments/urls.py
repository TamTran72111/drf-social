from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import CommentViewset, likeComment

router = DefaultRouter()
router.register('', CommentViewset)

urlpatterns = [
    path('like/<int:id>/', likeComment, name='comment-like'),
    path('<int:post_id>/', include(router.urls)),
]
