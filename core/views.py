from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "base.html")

def demo(request):
    return render(request, "demo.html")

def test(request):
    return render(request, "test.html")

def demo_simple(request):
    return render(request, "demo_simple.html")
