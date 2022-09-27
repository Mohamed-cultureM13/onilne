from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'
		
class ProductSerializer(serializers.ModelSerializer):
	categories = CategorySerializer(Many = True, Required = False)
	
	class Meta:
		model = Product
		fields = '__all__'
