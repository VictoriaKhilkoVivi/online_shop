from rest_framework import viewsets

from .serializers import ProductSerializer
from shop.categories.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
