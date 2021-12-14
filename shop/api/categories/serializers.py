from rest_framework import serializers

from shop.categories.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name'
            'price'
            'content'
            'categories'
        ]
