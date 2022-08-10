from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    content = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User, related_name='posts',
                             on_delete=models.CASCADE, default=None)
