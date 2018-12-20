from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from forum.models import *

# Create your views here.
from forum.forms import Registration


def index(request):
    posts = Post.objects.all()
    context = {'posts': posts}
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
    posts = Post.objects.all()
    context = {'posts': posts}
    return None


def tags(request):
    return None


def users(request):
    return None
