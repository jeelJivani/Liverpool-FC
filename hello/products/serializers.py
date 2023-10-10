from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
       #  fields = '__all__'
        exclude = ['id']



class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Quantity
        exclude = ['id']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ['id']



class ProductSerializer(serializers.ModelSerializer):
    category=CategorySerializer()
    quantity = QuantitySerializer()
    class Meta:
        model = Product
       #  fields = '__all__'
        exclude = ['id']



