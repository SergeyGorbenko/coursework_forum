from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='avatars', blank=True, null=True)
    count_posts = models.IntegerField(default=0)
    count_tags = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, unique=True)
    context = models.TextField(default='', blank=True, null=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return '#' + self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=100, unique=True, error_messages={'unique': "This theme has already exist."})
    context = models.TextField(default='', blank=True, null=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def display_tags(self):
        return '\n'.join(['#' + genre.name for genre in self.tags.all()[:3]])

    display_tags.short_description = 'Tags'

    def __str__(self):
        return self.theme


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    context = models.TextField()
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.theme + ' - ' + self.context


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    authors = models.CharField(max_length=255, blank=True, null=True)
    edition = models.DateField(blank=True, null=True)
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='books', blank=True, null=True,
                            validators=[FileExtensionValidator(
                                allowed_extensions=['pdf', 'txt', 'doc', 'epub', 'djvu', 'fb2'])])
    create = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-create"]

    def __str__(self):
        return self.name
