from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = SimpleRouter()
router.register("posts", PostViewSet)
router.register("groups", GroupViewSet)
router.register(r"^posts/(?P<post_id>\d+)/comments", CommentViewSet, basename='comments')
router.register("follow", FollowViewSet, basename='follow')

urlpatterns = [
    path("v1/", include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
