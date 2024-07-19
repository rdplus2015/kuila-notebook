from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def listview(request):
    return HttpResponse('hello, everything works')