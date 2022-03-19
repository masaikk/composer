from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def my(request):
    return HttpResponse('My')


def mainPage(request):
    return HttpResponse('Welcome to Composer')
