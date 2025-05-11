from rest_framework import serializers

from post.models import Post, Comment
from post.validators import WordValidator


class PostSerializer(serializers.ModelSerializer):
    title = serializers.CharField(validators=[WordValidator])

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
