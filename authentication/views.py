from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from .serializers import LoginSerializer, RegisterSerializer, LoginResponseSerializer


class Register(CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()


class Login(GenericAPIView):
    serializer_class = LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(username=serializer.data['username'])[0]

        if user is None or not User.check_password(user, serializer.data['password']):
            return Response('Username or password is incorrect!', status=status.HTTP_401_UNAUTHORIZED)

        userInfoSerializer = LoginResponseSerializer(user)

        dt = datetime.now() + timedelta(days=2)

        token = jwt.encode({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'is_superuser': user.is_superuser,
            'exp': datetime.now() + timedelta(days=2),
        }, settings.SECRET_KEY, algorithm='HS256')

        return Response(data={'user': userInfoSerializer.data, 'token': token}, status=status.HTTP_200_OK)
