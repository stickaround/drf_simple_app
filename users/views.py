from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import UserSerializer


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request):
        self.queryset = User.objects.exclude(id=request.user.id)
        serializer = UserSerializer(self.queryset, many=True)
        return Response(serializer.data)
