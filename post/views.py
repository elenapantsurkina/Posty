from rest_framework import generics, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from post.models import Post, Comment
from post.serializers import PostSerializer, CommentSerializer
from post.paginations import CustomPagination
from post.permissions import AuthorOrManager


class PostListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    pagination_class = CustomPagination


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostUpdateAPIView(generics.UpdateAPIView):
    serializer_class = PostSerializer
    permission_classes = [AuthorOrManager]
    queryset = Post.objects.all()


class PostDestroyAPIVIew(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [AuthorOrManager]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
