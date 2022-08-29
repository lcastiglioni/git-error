from itertools import product
from math import prod
from django.shortcuts import render, redirect
from meat.models import Products
from bakery.models import Bakeries
from drink.models import Drinks
from cart.cart import Cart
# Create your views here.

# def test(request):
#     meat = Products.objects.all()
#     drink = Drinks .objects.all()
#     bakery= Bakeries.objects.all()
#     dic = meat.union(drink, bakery)
#     context = {	
#         'cart_all': dic
#                         }
#     return render(request, "test.html", context=context)

def add_product(request, product_id):
    cart = Cart(request)
    product1 = Products.objects.get(id=product_id)
    product2 = Drinks.objects.get(id=product_id)
    product3 = Bakeries.objects.get(id=product_id)
    product = product1.union(product2, product3)
    if product.unic == "b":
        cart.add(product3)
    if product.unic == "m":
        cart.add(product1)
    elif product.unic == "d":
        cart.add(product2)

    # if product1 == "m":
    #     cart.add(product1)
    # elif product2 == "d":
    #     cart.add(product2)
    # elif product3 == "b":
    #     cart.add(product3)
    # return redirect("test")

def delete_product(request, product_id):
    cart = Cart(request)
    product1 = Products.objects.get(id=product_id)
    product2 = Drinks.objects.get(id=product_id)
    product3 = Bakeries.objects.get(id=product_id)
    product = product1.union(product2, product3)
    if product.unic == "b":
        cart.delete(product3)
    elif product.unic == "m":
        cart.delete(product1)
    elif product.unic == "d":
        cart.delete(product2)
    return redirect("test")


def subtract_product(request, product_id):
    cart = Cart(request)
    product1 = Products.objects.get(id=product_id)
    product2 = Drinks.objects.get(id=product_id)
    product3 = Bakeries.objects.get(id=product_id)
    product = product1.union(product2, product3)
    if product.unic == "b":
        cart.subtract(product3)
    elif product.unic == "m":
        cart.subtract(product1)
    elif product.unic == "d":
        cart.subtract(product2)
    return redirect("test")

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return redirect("test")


def test(request):
    
    meat = Products.objects.all()
    drink = Drinks .objects.all()
    bakery = Bakeries.objects.all()
    dic = meat.union(drink, bakery)
    context = {
        'products': dic
    }
    
    return render(request, "test2.html", context=context)
