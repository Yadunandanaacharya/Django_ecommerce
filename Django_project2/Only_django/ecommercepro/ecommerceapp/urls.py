from django.urls import path
from . import views

urlpatterns = [
    path('',views.ecommercestore, name = 'mainstore'),
    path('cart/',views.cart,name= 'cart'),
    path('checkout/',views.checkout, name = 'checkout')
    
]