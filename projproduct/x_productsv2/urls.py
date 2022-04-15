from django.urls import path, include
# from products.api_view import ProductDetailsApiViewSet, ProductDetailsESSearchApiViewSet, ProductDetailsByIdESSearchApiViewSet, ProductsListApiv2, ProductDetailApi2
from productsv2.api_view import ProductsListApiv2, ProductDetailApi2
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r'api', ProductDetailsApiViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('es-search/<str:query>/', ProductDetailsESSearchApiViewSet.as_view()),
    # path('id-es-search/<str:query>/', ProductDetailsByIdESSearchApiViewSet.as_view()),

    path('apiv2-list/', ProductsListApiv2.as_view()),
    path('apiv2-details/<int:pk>/', ProductDetailApi2.as_view()),
]