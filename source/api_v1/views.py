from django.shortcuts import render
from rest_framework.permissions import SAFE_METHODS
from rest_framework.viewsets import ModelViewSet

from api_v1.serializers import CommentSerializer
from webapp.models import Comment


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        else:
            return super().get_permissions()