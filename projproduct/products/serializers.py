from products.models import ProductDetails
from rest_framework import serializers


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ['id', 'name', 'price', 'quantity']

