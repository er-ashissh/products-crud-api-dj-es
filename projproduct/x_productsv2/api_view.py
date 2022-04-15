from django.http import HttpResponse
from django.http import JsonResponse
from elasticsearch_dsl import Q
from productsv2.es_documents import ProductDetailsDocument
from productsv2.models import ProductDetailsv2
from productsv2.serializers import ProductDetailsv2Serializer
from rest_framework import routers, serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import abc
import json, logging

logger = logging.getLogger(__name__)


class ProductsListApiv2(APIView):

    def post(self, request, format=None):
        products = ProductDetailsv2.objects.all()
        serializer = ProductDetailsv2Serializer(products)
        return Response(serializer.data)


    def get(self, request, format=None):
        products = ProductDetailsv2.objects.all()
        logger.debug(f'---products: {products}')
        return Response({})


class ProductsListApiv2(APIView):

    def post(self, request, format=None):
        serializer = ProductDetailsv2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        products = ProductDetailsv2.objects.all()
        serializer = ProductDetailsv2Serializer(products, many=True)
        return Response(serializer.data)


class ProductDetailApi2(APIView):
    """
    Retrieve, update or delete a products instance.
    """
    def get_object(self, pk):
        try:
            return ProductDetailsv2.objects.get(pk=pk)
        except ProductDetailsv2.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductDetailsv2Serializer(products)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductDetailsv2Serializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        products = self.get_object(pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  