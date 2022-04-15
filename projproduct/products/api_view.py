from django.http import HttpResponse
from django.http import JsonResponse
from elasticsearch_dsl import Q
from products.es_documents import ProductDetailsDocument
from products.es_documents import ProductDetailsESDocument
from products.models import ProductDetails
from products.serializers import ProductDetailsSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import abc
import json, logging

logger = logging.getLogger(__name__)


class ProductDetailsApiViewSet(viewsets.ModelViewSet):
    document = ProductDetailsDocument
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer


class PaginatedElasticSearchAPIView(APIView, LimitOffsetPagination):
    serializer_class = None
    document_class = None

    @abc.abstractmethod
    def generate_q_expression(self, query):
        """This method should be overridden and return a Q() expression."""

    def get(self, request, query):
        try:
            q = self.generate_q_expression(query)
            search = self.document_class.search().query(q).sort('id')
            response = search.execute()
            # print(f'Found {response.hits.total.value} hit(s) for query: "{query}"')
            results = self.paginate_queryset(response, request, view=self)
            serializer = self.serializer_class(results, many=True)
            return self.get_paginated_response(serializer.data)
        except Exception as e:
            return HttpResponse(e, status=500)


class ProductDetailsESSearchApiViewSet(PaginatedElasticSearchAPIView):
    serializer_class = ProductDetailsSerializer
    document_class = ProductDetailsDocument

    def generate_q_expression(self, query):
        if query == '*':
            qry = Q('match_all')
        else:
            qry = Q('multi_match', query=query, fields=['name'], fuzziness='auto')
        return qry


class ProductDetailsByIdESSearchApiViewSet(PaginatedElasticSearchAPIView):
    serializer_class = ProductDetailsSerializer
    document_class = ProductDetailsDocument

    def generate_q_expression(self, query):
        return Q('multi_match', query=query, fields=['id'])


class ProductsListApiv2(APIView):

    def post(self, request, format=None):
        
        # products__objs = ProductDetails.objects.all()
        # logger.debug(f'---products: {products__objs}')
        # products_json = ProductDetailsSerializer(products__objs)
        # return Response({'data': products_json})
        # # return Response(products)

        # products_objs = ProductDetails.objects.all()
        # logger.debug(f'---products: {products_objs}')
        # products_json = ProductDetailsSerializer(products_objs)
        # return JsonResponse({'data': products_json.data})

        products = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(products)
        return Response(serializer.data)


    def get(self, request, format=None):
        
        # products__objs = ProductDetails.objects.all()
        # logger.debug(f'---products: {products__objs}')
        # products_json = ProductDetailsSerializer(products__objs)
        # return Response({'data': products_json})
        # # return Response(products)

        # products_objs = ProductDetails.objects.all()
        # logger.debug(f'---products: {products_objs}')
        # products_json = ProductDetailsSerializer(products_objs)
        # return JsonResponse({'data': products_json.data})

        # products = ProductDetails.objects.all()
        products = ProductDetails.objects.all()
        logger.debug(f'---products: {products}')
        # serializer = ProductDetailsSerializer(products, many=True)
        # return Response(serializer.data)
        return Response({})




class ProductsListApiv2(APIView):

    def post(self, request, format=None):
        serializer = ProductDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        products = ProductDetails.objects.all()
        serializer = ProductDetailsSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailApi2(APIView):
    """
    Retrieve, update or delete a products instance.
    """
    def get_object(self, pk):
        try:
            return ProductDetails.objects.get(pk=pk)
        except ProductDetails.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductDetailsSerializer(products)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        products = self.get_object(pk)
        serializer = ProductDetailsSerializer(products, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        products = self.get_object(pk)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  


class ProductESListApiv2View(APIView, LimitOffsetPagination):
    product_search_serializer = ProductDetailsSerializer
    search_document = ProductDetailsESDocument

    def get(self, request, query=""):
        try:
            # creating query instance
            # q = Q(
            #     "match_all",
            #     query=query,
            #     fields=[
            #         "name"
            #         ],
            # )
            q = Q('match_all')

            search = self.search_document.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.product_search_serializer(results, many=True)

            return self.get_paginated_response(serializer.data)
        except:
            return Response({"msg":f"data not found for product name {query}!!"}, status=status.HTTP_404_NOT_FOUND)


class ProductSearchApiv2View(APIView, LimitOffsetPagination):
    product_search_serializer = ProductDetailsSerializer
    search_document = ProductDetailsESDocument

    def get(self, request, query):
        try:
            # creating query instance
            q = Q(
                "multi_match",
                query=query,
                fields=[
                    "name"
                    ],
            )

            search = self.search_document.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request, view=self)
            serializer = self.product_search_serializer(results, many=True)

            return self.get_paginated_response(serializer.data)
            
        except:
            return Response({"msg":f"data not found for product name {query}!!"}, status=status.HTTP_404_NOT_FOUND)

