from rest_framework import serializers
from store.models import Category, Post





class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', )


class ParentCategoriesSerializer(serializers.ModelSerializer):
    children = CategoriesSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('title', 'children')


class VipPostsSerializer(serializers.ModelSerializer):
    location = serializers.StringRelatedField(source = 'address.title')
    class Meta:
        model = Post
        fields = ('main_photo', 'price', 'location', 'created_at')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'main_photo', 'description', 'price')





