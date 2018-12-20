from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forum.models import *

# Create your views here.
from forum.forms import Registration


def home(request):
    context = {}
    return render(request, 'index.html', context=context)


def registration(request):
    context = {}
    if request.method == 'POST':
        form = Registration(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pass_1 = form.cleaned_data['password1']
            pass_2 = form.cleaned_data['password2']
            context['profile'] = {'username': username,
                                  'email': email,
                                  'pass_1': pass_1,
                                  'pass_2': pass_2}
            try:
                if User.objects.get(username=username) and User.objects.get(email=email):
                    context['error'] = ['user_exist']
            except User.DoesNotExist:
                if pass_1 != pass_2:
                    context['error'] = ['passwords_not_match']
                else:
                    user = User(username=username, email=email, password=pass_1)
                    user.save()
                    HttpResponseRedirect('/login/')

    context['form'] = Registration()
    return render(request, 'registration/registration.html', context=context)
