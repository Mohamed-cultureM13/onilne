from rest_framework import generics
from .models import Category, Product
from serializers import CategorySerializer, ProductSerializer

class ProductList(generics.ListCreateAPIView):
	queryset = Category.objects.all()
	serializer_class = CategorySerializer
	
class ProductDetail(generics.RetrieveDestroyAPIView):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

class ChooseProduct(generics.CreateAPIView):
	serializer_class = ProductSerializer
