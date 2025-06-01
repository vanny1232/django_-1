from django.urls import path 
from . import views

urlpatterns = [
    path('', views.IndexViewsHome,name='home'),
    path('about/',views.Aboutus,name='About'),
    path('contact/',views.Contact,name='Contact'),
    path('customer/',views.customer,name='customer'),
    path('product/',views.products,name='product'),
    path('index/',views.IndexViews,name='index'),
    path('index/<int:id>',views.IndexViews,name='index'),
    path('menus/<int:id>',views.MenuDetail,name='menu'),
    
]