# serializers.py
from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = '__all__'

    def get_author(self, obj):
        profile = obj.author.profile
        author_data = {'id': obj.author.id, 'name': obj.author.username}
        
        if profile and profile.upload:
            author_data['img'] = profile.upload.url
            
        return author_data

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('id', 'name', 'manufacturer', 'average_cost', 'category', 'release_date', 'description', 'upload', 'reviews')
        
class ProductListSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'manufacturer', 'average_cost', 'category', 'release_date', 'description', 'upload', 'reviews')
        
    def get_reviews(self, obj):
        reviews = obj.review_set.all()[:3]
        return ReviewSerializer(reviews, many=True).data