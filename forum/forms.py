from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from forum.models import *

from forum.models import Post, Tag


class Registration(UserCreationForm):
    email = forms.EmailField(label='Email address', required=False, help_text='Not necessary ')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("A user with this email already exists.")
        except:
            pass

        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')

        if not password1:
            raise forms.ValidationError("You have ti verify your password")
        if password != password1:
            raise forms.ValidationError("Your passwords doesn't match")
        return password1


class CreatePost(ModelForm):
    class Meta:
        model = Post
        fields = ('theme', 'context')


class CreateTag(ModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'context')


class ChangeProfile(forms.Form):
    username = forms.CharField(max_length=150, required=True, label='Username')
    first_name = forms.CharField(label='First name', max_length=30, required=False)
    last_name = forms.CharField(label='Last name', max_length=150, required=False)
    about = forms.CharField(label='About', max_length=255, required=False)
    email = forms.EmailField(label='Email address', required=False)
    photo = forms.ImageField()

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise forms.ValidationError("A user with this name already exists.")
        except:
            pass

        return username
