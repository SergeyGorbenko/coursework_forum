from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from forum.models import Post, Tag


class Registration(UserCreationForm):
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ('theme', 'context')


class CreateTag(ModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'context')
