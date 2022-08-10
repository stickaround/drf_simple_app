from django.urls import path
from .views import Login, Register
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register', Register.as_view(), name='auth-register'),
    path('login', Login.as_view(), name='auth-login'),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view())
]
