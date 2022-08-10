from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post


class UserSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class PostSerializer(serializers.ModelSerializer):
    user = UserSummarySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user']
