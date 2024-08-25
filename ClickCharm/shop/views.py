from django.shortcuts import render
from django.http import HttpResponse
from .models import product  
from math import ceil


# Create your views here.
def index(request):
    products= product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    # params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    allprods = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allprods' : allprods }
    return render(request,"shop/index.html", params)
def about(request):
    return render(request, 'shop/about.html')
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



