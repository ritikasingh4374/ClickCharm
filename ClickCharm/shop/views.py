from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')
def contact(request):
    return render(request, 'shop/index2.html')
def tracker(request):
    return render(request, 'shop/index.html')
def search(request):
    return render(request, 'shop/index.html')
def productview(request):
    return render(request, 'shop/index.html')
def checkout(request):
    return render(request, 'shop/index.html')
