from django.urls import path
from .views import Login, Register

urlpatterns = [
    path('register', Register.as_view(), name='auth-register'),
    path('login', Login.as_view(), name='auth-login'),
]
