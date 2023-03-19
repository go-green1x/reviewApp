from django.shortcuts import render

from rest_framework import viewsets
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer, ProductListSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        else:
            return ProductSerializer
    
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)