from django.urls import path 
from . import views_ogani
urlpatterns = [
    path('',views_ogani.home, name='homeOgani'),
    path('shop-details/', views_ogani.shopDetail, name='shopDetail'),
    path('shoping-cart/', views_ogani.shopingCart, name='shopingCart'),
]