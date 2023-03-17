# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class ModelProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'address', 'city', 'country', 'upload')

class UserSerializer(serializers.ModelSerializer):
    profile = ModelProfileSerializer()

    class Meta:
        model = User
        fields = ('username','first_name','last_name', 'email', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_new_password = serializers.CharField(required=True)
    
class UserDetails(serializers.ModelSerializer):
    email = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ('email', 'first_name', 'last_name', 'date_of_birth', 'address', 'city', 'country', 'upload')

    def update(self, instance, validated_data):
        user = instance.user
        user.email = validated_data.get('email', user.email)
        user.first_name = validated_data.get('first_name', user.first_name)
        user.last_name = validated_data.get('last_name', user.last_name)
        user.save()

        instance = super().update(instance, validated_data)

        return instance
