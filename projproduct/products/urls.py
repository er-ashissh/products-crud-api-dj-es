from django.urls import path, include
from products.api_view import ProductDetailsApiViewSet, ProductDetailsESSearchApiViewSet, ProductDetailsByIdESSearchApiViewSet, ProductsListApiv2, ProductDetailApi2, ProductESListApiv2View, ProductSearchApiv2View
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api', ProductDetailsApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('es-search/<str:query>/', ProductDetailsESSearchApiViewSet.as_view()),
    path('id-es-search/<str:query>/', ProductDetailsByIdESSearchApiViewSet.as_view()),

    path('apiv2-list/', ProductsListApiv2.as_view()),
    path('apiv2-details/<int:pk>/', ProductDetailApi2.as_view()),
    path('apiv2-es-list/', ProductESListApiv2View.as_view(), name='product-es-list-v2'),
    path('apiv2-search/<str:query>/', ProductSearchApiv2View.as_view(), name='product-es-search-v2'),
]