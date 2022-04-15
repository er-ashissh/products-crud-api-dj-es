from django.urls import path, include
from products.api_view import ProductDetailsApiViewSet, ProductDetailsESSearchApiViewSet, ProductDetailsByIdESSearchApiViewSet, ProductsListApiv2
from rest_framework import routers


urlpatterns = [

    path('apiv2-list/', ProductsListApiv2.as_view()),
    path('apiv2-details', ProductDetailsByIdESSearchApiViewSet.as_view()),
]