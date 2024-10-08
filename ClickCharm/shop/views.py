from django.shortcuts import render
from django.http import HttpResponse
from .models import product  
from math import ceil


# Create your views here.
def index(request):
    # products= product.objects.all()
    # n= len(products)
    # nSlides= n//4 + ceil((n/4) + (n//4))
    allprods =[]
    catprods = product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nSlides= n//4 + ceil((n/4) + (n//4))
        allprods.append([prod, range(1, nSlides), nSlides])
    # params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    # allprods = [[products, range(1, nSlides), nSlides], [products, range(1, nSlides), nSlides]]
    params = {'allprods' : allprods }
    return render(request,"shop/index.html", params)
def about(request):
    return render(request, 'shop/about.html')
def contact(request):
    if request.method == 'post':
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        print(name, email, phone, desc)
        contacts = contact(name=name, email=email, phone=phone, desc=desc)
        contacts.save()
    return render(request, 'shop/Contact.html')
def tracker(request):
    return render(request, 'shop/tracker.html')
def search(request):
    return render(request, 'shop/search.html')
def prodview(request, myid):
    prod = product.objects.filter(id = myid)
    print(prod)
    return render(request, 'shop/prodview.html', {'prod' : prod[0]})
def checkout(request):
    return render(request, 'shop/checkout.html')



