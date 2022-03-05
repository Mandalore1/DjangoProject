from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "GET":
        return HttpResponse("Hello, world!")
