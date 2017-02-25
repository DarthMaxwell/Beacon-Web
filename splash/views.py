from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<link rel=\"shortcut icon\" type=\"image/png\" href=\"/favicon.ico\"/>Hello, world.")
