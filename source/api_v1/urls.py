from django.urls import path, include
from rest_framework import routers

from api_v1.views import CommentViewSet, Like, Dislike, CanLike

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
    path('like/<int:pk>/', Like.as_view(), name='like_photo'),
    path('dislike/<int:pk>/', Dislike.as_view(), name='dislike_photo'),
    path('can_like/<int:pk>/', CanLike.as_view(), name='can_like_photo')
]