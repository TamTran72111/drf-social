from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewset

router = DefaultRouter()
router.register('', PostViewset)

urlpatterns = [
    path('', include(router.urls)),
]
