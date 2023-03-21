from django.shortcuts import render

from rest_framework import viewsets
from .models import Product, Review, Info
from .serializers import ProductSerializer, ReviewSerializer, ProductListSerializer, ConatactMailSerializer
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.mail import send_mail

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
        email_from = Info.objects.filter(attribute='email', status=1)[0].value
        email_from_password = Info.objects.filter(attribute='emailpassword', status=1)[0].value

        recipient_list=[email_from,]
        try:
            send_mail(subject, message, user.email, recipient_list, fail_silently=False, auth_user=email_from, auth_password=email_from_password)
        except:
            pass
        return Response(True, status=status.HTTP_200_OK)