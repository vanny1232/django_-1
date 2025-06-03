from django.urls import path 
from . import views_ogani
urlpatterns = [
    path('',views_ogani.home, name='homeOgani'),
    path('shop-details/', views_ogani.shopDetail, name='shopDetail'),
    path('shoping-cart/', views_ogani.shopingCart, name='shopingCart'),
    path('shoping-grid/', views_ogani.shopingGrid, name='shopingGridOgani'),    
    path('about-us/', views_ogani.about, name='aboutOgani'),
    path('contact-us/', views_ogani.contact, name='contactOgani'),
    path('checkout/', views_ogani.checkout, name='checkoutOgani'),
    path('blog/', views_ogani.blog, name='blogOgani'),
    path('blog-details/', views_ogani.blogDetails, name='blogDetailsOgani'),

]