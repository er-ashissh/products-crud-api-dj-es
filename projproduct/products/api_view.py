from django.http import HttpResponse
from elasticsearch_dsl import Q
from products.es_documents import ProductDetailsDocument
from products.models import ProductDetails
from products.serializers import ProductDetailsSerializer
from rest_framework import routers, serializers, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
import abc


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

