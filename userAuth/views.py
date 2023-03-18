# from django.shortcuts import render

from django.contrib.auth import login, authenticate, update_session_auth_hash
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from knox.auth import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, ChangePasswordSerializer, ModelProfileSerializer, UserDetails
from .models import Profile
# Create your views here.

class UserCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class LoginView(KnoxLoginView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        userDetail = {
            'username' : request.user.username,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email,
            'profile' : ModelProfileSerializer(Profile.objects.get(user=request.user)).data
        }
        response = super(LoginView, self).post(request, format=None)
        response.data['userDetails'] = userDetail
        return response

class UserIsAuthenticated(APIView):

    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        # simply delete the token to force a login
        return Response(True, status=status.HTTP_200_OK)

class ChangePassword(APIView):
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = request.user
        old_password = serializer.data.get('old_password')
        new_password = serializer.data.get('new_password')
        confirm_new_password = serializer.data.get('confirm_new_password')

        if not user.check_password(old_password):
            return Response({'old_password': 'Incorrect password.'}, status=status.HTTP_400_BAD_REQUEST)

        if new_password != confirm_new_password:
            return Response({'new_password': "New passwords don't match."}, status=status.HTTP_400_BAD_REQUEST)

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)

        return Response({'message': 'Password updated successfully.'}, status=status.HTTP_200_OK)

class ProfileUpdateView(APIView):
    serializer_class = UserDetails
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        user_profile = request.user.profile
        serializer = self.serializer_class(user_profile, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)