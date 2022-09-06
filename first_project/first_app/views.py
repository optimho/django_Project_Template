from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello World 1")


def alternative(request):
    return HttpResponse("Hello World 2")
