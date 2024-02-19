from rest_framework import generics

from store.models import Category, Post
from store.serializers import ParentCategoriesSerializer, PostDetailSerializer, VipPostsSerializer


class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ParentCategoriesSerializer


class PostDetailApiView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class StatusPostListApiView(generics.ListAPIView):
    queryset = Post.objects.filter(PlanDetail__code="VIP")
    serializer_class=VipPostsSerializer
