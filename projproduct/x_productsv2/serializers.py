from productsv2.models import ProductDetailsv2
from rest_framework import serializers


class ProductDetailsv2Serializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=20) 
    price = serializers.IntegerField() 
    quantity = serializers.IntegerField() 

    class Meta:
        model = ProductDetailsv2
        # fields = '__all__'
        fields = ['id', 'name', 'price', 'quantity']

