# blog/modles.py

from django.db import models
from django.core.validators import MinLengthValidator

class Post(models.Model):
    author_name = models.CharField(max_length=20, default="user")
    title = models.CharField(max_length=100, validators=[MinLengthValidator(3)])
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
