from django.urls import path, include
from rest_framework import routers

from api_v1.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r'comment', CommentViewSet)
app_name = 'api_v1'

urlpatterns = [
    path('', include(router.urls)),
]