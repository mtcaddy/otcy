from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello, world. You arere at the polls index.')
