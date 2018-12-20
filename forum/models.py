from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=15)
    context = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '#' + self.name


class Post(models.Model):
    theme = models.CharField(max_length=100)
    context = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.theme


class Comment(models.Model):
    context = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.theme + ' - ' + self.context
