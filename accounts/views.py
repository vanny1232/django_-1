from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.

def home(request):
    costomer = models.Customer.objects.all()
    costomer_byid=models.Customer.objects.exclude(id=1)
    context={
        'costomer':costomer,
        'costomer_byid':costomer_byid
    }
    return render(request,'homepage.html',context)

def products(request):
    return render(request,'Products_page.html')

def customer(request):
    return render(request,'Customer_page.html')

def IndexViews(request,id):
    # រំលង  Ex :id =2 រំលងជួរទី២
    cusex = models.Customer.objects.exclude(id=2) 
    filteruser = models.Customer.objects.filter(id=200).exists()
    get = models.Customer.objects.get(id=id)
    userfis =models.Customer.objects.first()
    lastusr =models.Customer.objects.last()
    oderbyiddoc =models.Customer.objects.order_by('-id')
    oderbyid =models.Customer.objects.order_by('id')
    cus = models.Customer.objects.all()
    usercount = models.Customer.objects.count()
    context = {
        'get':get,
        'lastusr':lastusr,
        'filteruser':filteruser,
        'userfis':userfis,
        'usercount':usercount,
        'oderbyiddoc':oderbyiddoc,
        'oderbyid':oderbyid,
        'customer':cus,
        'cusex':cusex
    }
    return render(request,"accounts/index.html",context)


def IndexViewsHome(request):
    Benner = models.Image.objects.filter(ImageTypeID=1)
    Logo = models.Image.objects.filter(ImageTypeID=2)
    Slide_Show = models.Image.objects.filter(ImageTypeID=3)
    Slide_Left= models.Image.objects.filter(ImageTypeID=4)
    Slide_Right = models.Image.objects.filter(ImageTypeID=5)
    Footer = models.Image.objects.filter(ImageTypeID=6)

    Menu = models.Menu.objects.all()

    context ={
        'Menu':Menu,
        'Benner':Benner,
        'Logo':Logo,
        'Slide_Show':Slide_Show,
        'Slide_Left':Slide_Left,
        'Slide_Right':Slide_Right,
        'Footer':Footer,

    }
    return render(request,"accounts/indexfrom.html",context)


def MenuDetail(request,id):

    menu_detail = models.MenuDetail.objects.filter(MenuID=id)
    Benner = models.Image.objects.filter(ImageTypeID=1)
    Logo = models.Image.objects.filter(ImageTypeID=2)
    Slide_Show = models.Image.objects.filter(ImageTypeID=3)
    Slide_Left= models.Image.objects.filter(ImageTypeID=4)
    Slide_Right = models.Image.objects.filter(ImageTypeID=5)
    Footer = models.Image.objects.filter(ImageTypeID=6)

    Menu = models.Menu.objects.all()

    context ={
        'Menu':Menu,
        'Benner':Benner,
        'Logo':Logo,
        'Slide_Show':Slide_Show,
        'Slide_Left':Slide_Left,
        'Slide_Right':Slide_Right,
        'Footer':Footer,
         'menu_detail':menu_detail

    }
 
    return render(request,"accounts/MenuDetail.html",context)

def Aboutus(request):
    return render(request,"accounts/aboutas.html")

def Contact(request):
    return render(request,"accounts/contact.html")