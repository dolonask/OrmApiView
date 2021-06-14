from rest_framework import serializers
from .models import ProductType


class ProductType_serializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'
        # exclude
