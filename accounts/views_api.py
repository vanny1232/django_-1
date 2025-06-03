from . import models
from rest_framework import generics
from . import serializers
# Create your views here.

# ListCreateAPIView provides GET (list) and POST (create) actionsclass 

class ProductsListCreate(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()   
    serializer_class = serializers.Products

# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions

class ProductsUpdate(generics.RetrieveUpdateDestroyAPIView):    
    queryset = models.Product.objects.all()
    serializer_class = serializers.Products

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()   
    serializer_class = serializers.Categorys

# RetrieveUpdateDestroyAPIView provides GET (retrieve), PUT (update), DELETE (destroy) actions

class CategoryUpdate(generics.RetrieveUpdateDestroyAPIView):    
    queryset = models.Category.objects.all()
    serializer_class = serializers.Categorys