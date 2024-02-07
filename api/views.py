from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from api.models import Product, User
from api.serializers import ProductSerializer, UserSerializer

class UserListApiview(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserdetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class productListApiview(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class ProductdetailApiview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer