from rest_framework import serializers
from webapp.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format="%Y-%m-%d %H:%M:%S")
    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','text', 'author', 'photo', 'created_at')

    def save(self, **kwargs):
        self.validated_data['author'] = self.context['request'].user
        return super().save()
