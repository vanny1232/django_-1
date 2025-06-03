from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home(request):
    return render(request,'Ogani/index.html')


def shopDetail(request):
    return render(request, 'Ogani/shop-details.html')


def shopingCart(request):
    return render(request, 'Ogani/shoping-cart.html')


def shopingGrid(request):
    return render(request, 'Ogani/shoping-grid.html')

def contact(request):
    return render(request, 'Ogani/contact.html')

def checkout(request):
    return render(request, 'Ogani/checkout.html')

def blog(request):
    return render(request, 'Ogani/blog.html')

def blogDetails(request):
    return render(request, 'Ogani/blog-details.html')


def about(request):
    return render(request, 'Ogani/aboutUs.html')