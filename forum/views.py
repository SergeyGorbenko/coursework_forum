from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from forum.models import *

# Create your views here.
from forum.forms import Registration


def index(request):
    context = {}
    return render(request, 'index.html', context=context)


def registration(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('')
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
            return HttpResponseRedirect('/post/')
        else:
            # If there were errors, we render the form with these
            # errors
            return render(request, 'registration/registration.html', {'form': form})
    return render(request, 'registration/registration.html', {'form': Registration()})
