from django.db import models
from django.conf import settings

class Post(models.Model) :
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")

    def __str__(self) :
        return self.title


class Comment(models.Model) :
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.content