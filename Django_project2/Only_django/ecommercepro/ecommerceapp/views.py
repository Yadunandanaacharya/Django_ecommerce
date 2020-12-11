from django.shortcuts import render
from . models import *
# Create your views here.
def ecommercestore(request):
    products = Product.objects.all()
    context={'products':products}
    return render(request, 'ecommerceapp/ecommercestore.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        # order = {'get_cart_total': 0, 'get_cart_items': 0}
    context = {'items': items}
    return render(request, 'ecommerceapp/cart.html', context)

def checkout(request):
    # if request.user.is_authenticated:
    #     customer = request.user.customer
    #     order, created = Order.objects.get_or_create(customer=customer, complete=False)
    #     items = order.orderitem_set.all()
    # else:
    #     items = []
    #     order = {'get_cart_total': 0, 'get_cart_items': 0}
    # context = {'items': items, 'order': order}
    return render(request, 'ecommerceapp/checkout.html')#, context)