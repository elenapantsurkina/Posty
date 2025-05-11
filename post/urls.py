from django.urls import path

from post.apps import PostConfig
from post.views import CommentViewSet, PostListAPIView, PostCreateAPIView, PostUpdateAPIView, PostDestroyAPIVIew
from rest_framework.routers import DefaultRouter

app_name = PostConfig.name


router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')

urlpatterns = [

    path('', PostListAPIView.as_view(), name='article_list'),
    path('create/', PostCreateAPIView.as_view(), name='article_create'),
    path('update/<int:pk>/', PostUpdateAPIView.as_view(), name='article_update'),
    path('update/<int:pk>/', PostUpdateAPIView.as_view(), name='article_update'),
    path('delete/<int:pk>/', PostDestroyAPIVIew.as_view(), name='article_delete'),


] + router.urls
