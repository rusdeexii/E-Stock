from rest_framework import serializers
from .models import Product, Category, Unit

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    unit = UnitSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
