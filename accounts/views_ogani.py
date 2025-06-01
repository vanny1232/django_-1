from django.shortcuts import render
from django.http import HttpResponse
from . import models


def home(request):
    return render(request,'Ogani/index.html')
def shopDetail(request):
    return render(request, 'Ogani/shop-details.html')

def shopingCart(request):
    return render(request, 'Ogani/shoping-cart.html')