from django.shortcuts import render
from django.http import HttpResponse
from . models import Product, Contact
import math as m
# Create your views here.


def index(request):

    # n = len(products)
    # nslides = n//4+ m.ceil((n/4)-n//4)
    allProds = []
    categoryprods = Product.objects.values('category', 'id')
    categrys = {item['category'] for item in categoryprods}
    for i in categrys:
        prod = Product.objects.filter(category=i)
        n = len(prod)
        nslides = n//4 + m.ceil((n/4)-n//4)
        allProds.append([prod, range(1, nslides), nslides])

    # params = {'no_of_slides':nslides,'itemranges':range(1,nslides),'product':products}
    # allProds = [[products,range(1,nslides),nslides],
    #             [products,range(1,nslides),nslides]]
    params = {'allProds': allProds}
    return render(request, 'ecomshop/index.html', params)


def about(request):
    return render(request, 'ecomshop/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "ecomshop/contact.html")


def tracker(request):
    return render(request, 'ecomshop/tracker.html')


def search(request):
    return render(request, 'ecomshop/search.html')


def productview(request, myid):
    # Fetch the product using the id.
    product = Product.objects.filter(id=myid)
    return render(request, 'ecomshop/productview.html', {'product': product[0]})


def checkout(request):
    return render(request, 'ecomshop/checkout.html')
