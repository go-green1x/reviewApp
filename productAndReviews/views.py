from django.shortcuts import render

from rest_framework import viewsets
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer, ProductListSerializer, ConatactMailSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings

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
    
class ConatactMailViewSet(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = ConatactMailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        user = request.user
        email_from = settings.EMAIL_HOST_USER
        recipient_list=[email_from, user.email,]
        try:
            send_mail(subject, message, email_from, recipient_list, fail_silently=False)
        except:
            pass
        return Response(True, status=status.HTTP_200_OK)