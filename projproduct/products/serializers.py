from products.models import ProductDetails
from rest_framework import serializers


class ProductDetailsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=200) 
    price = serializers.IntegerField() 
    quantity = serializers.IntegerField() 

    class Meta:
        model = ProductDetails
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'quantity']

