from rest_framework import status
from rest_framework.permissions import SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from api_v1.serializers import CommentSerializer
from webapp.models import Comment, Photo
from webapp.models import LikeSystem


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        elif self.request.method == 'DELETE':
            if self.request.user.has_perm('webapp.delete_comment') or self.get_object().author == self.request.user:
                return []
        return super().get_permissions()


class Like(APIView):
    def patch(self, request, pk):
        try:
            LikeSystem.objects.get(user=request.user, photo_id=pk)
            return Response(data={"detail": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)
        except:
            LikeSystem.objects.create(user=request.user, photo_id=pk)
            return Response(data={"likes": Photo.objects.get(pk=pk).likes})


class Dislike(APIView):
    def patch(self, request, pk):
        try:
            like = LikeSystem.objects.get(user=request.user, photo_id=pk)
            like.delete()
            return Response(data={"likes": Photo.objects.get(pk=pk).likes})
        except:
            return Response(data={"detail": "Can not dislike"}, status=status.HTTP_400_BAD_REQUEST)


class CanLike(APIView):
    def get(self, request, pk):
        try:
            LikeSystem.objects.get(user=request.user, photo_id=pk)
            return Response(data={"can_like": 0}, status=status.HTTP_200_OK)
        except:
            return Response(data={"can_like": 1}, status=status.HTTP_404_NOT_FOUND)