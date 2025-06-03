from rest_framework import serializers

from .models import *

class Products(serializers.ModelSerializer):
    class Meta:        
        model = Product
        fields = ['id', 'productName', 'categoryID','price','productDescript','weight','availability','shipping','productImage']
class Categorys(serializers.ModelSerializer):
    class Meta:        
        model = Category
        fields = ['id', 'categoryName', 'categoryImage']