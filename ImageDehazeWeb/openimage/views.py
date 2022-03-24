from django.shortcuts import render

# Create your views here.

def homeView(request, *args, **kwargs):
    return render(request, "index(new).html", {})

def resultView(request, *args, **kwargs):
    return render(request, "results.html", {})