from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from forum.forms import Registration


def home(request):
    context = {}
    return render(request, 'index.html', context=context)


def registration(request):
    context = {'form': Registration()}
    return render(request, 'registration/registration.html', context=context)
