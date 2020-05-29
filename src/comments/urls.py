from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import CommentViewset

router = DefaultRouter()
router.register('', CommentViewset)

urlpatterns = [
    path('<int:post_id>/', include(router.urls)),
]
