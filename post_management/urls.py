from django.urls import path, include

urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('posts/', include('posts.urls')),
]
