from django.urls import path, include
from products.api_view import ProductDetailsApiViewSet, ProductDetailsESSearchApiViewSet, ProductDetailsByIdESSearchApiViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api', ProductDetailsApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('es-search/<str:query>/', ProductDetailsESSearchApiViewSet.as_view()),
    path('id-es-search/<str:query>/', ProductDetailsByIdESSearchApiViewSet.as_view()),
]