from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from forum.models import *

# Create your views here.
from forum.forms import Registration


def index(request):
    posts = Post.objects.all()
    context = {'count': posts.count(), 'posts': posts}
    return render(request, 'index.html', context=context)


def registration(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'GET':
        form = Registration()
        return render(request, 'registration/registration.html', {'form': form})
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/registration.html', {'form': form})


def posts(request):
    all_posts = Post.objects.all()
    form = CreateTag()
    context = {'posts': all_posts, 'form': form}
    return render(request, 'post/posts.html', context=context)


def tags(request):
    all_tags = Tag.objects.all()
    form = CreateTag()
    context = {'tags': all_tags, 'form': form}
    return render(request, 'tag/tags.html', context=context)


def users(request):
    all_users = UserProfile.objects.all()
    context = {'users': all_users}
    return render(request, 'user/users.html', context=context)


def create_post(request):
    return redirect('/posts/')


def create_tag(request):
    return redirect('/tags/')
