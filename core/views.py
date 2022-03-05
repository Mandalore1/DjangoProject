from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    if request.method == "GET":
        if "name" in request.GET:
            name = request.GET["name"]
        else:
            name = "world"

    return render(request, "hello.html", {"name": name})
