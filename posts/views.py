from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def list(self, request):
        if not request.user.is_superuser:
            self.queryset = Post.objects.filter(user_id=request.user.id)
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
