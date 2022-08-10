from django.contrib.auth.models import User
from django.contrib.auth import hashers
from rest_framework import serializers
from posts.models import Post


class PostSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content']


class UserSerializer(serializers.ModelSerializer):
    posts = PostSummarySerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email',
                  'is_active', 'is_superuser', 'password', 'posts']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data['email']
        instance.username = validated_data['username']
        instance.password = hashers.make_password(validated_data['password'])
        instance.save()
        return instance
