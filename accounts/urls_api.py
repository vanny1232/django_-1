from django.urls import path 
from . import views_api

urlpatterns = [
    path('products/', views_api.ProductsListCreate.as_view(), name='ApiproductsListCreate'),
    path('products/<int:pk>/', views_api.ProductsUpdate.as_view(), name='ApiproductsDetailUD'),
    path('category/', views_api.CategoryListCreate.as_view(), name='categoryListCreate'),
    path('category/<int:pk>/', views_api.CategoryUpdate.as_view(), name='categoryDetailUD'),
]