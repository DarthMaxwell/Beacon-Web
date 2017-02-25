from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("<link rel=\"shortcut icon\" type=\"image/png\" href=\"/favicon.ico\"/>Hello, world.")
