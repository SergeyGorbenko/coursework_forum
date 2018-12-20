from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
def home(request):
    context = {}
    return render(request, 'index.html', context=context)


def logout(request):
    return HttpResponseRedirect("/")
