# serializers.py
from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField(required=False)
    date_posted = serializers.DateTimeField(required=False)
    class Meta:
        model = Review
        fields = '__all__'

    def get_author(self, obj):
        profile = obj.author.profile
        author_data = {'id': obj.author.id, 'name': obj.author.username}
        
        if profile and profile.upload:
            author_data['img'] = profile.upload.url
            
        return author_data
    
    def create(self, validated_data):
        user = self.context['request'].user
        rating = validated_data.pop('rating')
        review = validated_data.pop('review')
        product_id = validated_data.pop('product')
        review = Review.objects.create(author=user, rating= rating, review= review, product_id=product_id.id)
        return review
    
    def update(self, instance, validated_data):
        if instance.author != self.context['request'].user:
            raise serializers.ValidationError({
                'review': 'You donot have permission to update this review',
                })
        instance.rating = validated_data.get('rating', instance.rating)
        instance.review = validated_data.get('review', instance.review)
        # instance.product = validated_data.get('product', instance.product)
        instance.save()
        return instance

    def delete(self, instance):
        instance.delete()

class ProductSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'manufacturer', 'average_cost', 'category', 'release_date', 'description', 'upload', 'reviews', 'avg_rating')
    
    def get_avg_rating(self, obj):
        ratings = [review.rating for review in obj.review_set.all()]
        if len(ratings) > 0:
            return sum(ratings) / len(ratings)
        else:
            return 0

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        return ReviewSerializer(reviews, many=True).data
        
class ProductListSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'manufacturer', 'average_cost', 'category', 'release_date', 'description', 'upload', 'reviews')
        
    def get_reviews(self, obj):
        reviews = obj.review_set.all()[:3]
        return ReviewSerializer(reviews, many=True).data
    
class ConatactMailSerializer(serializers.Serializer):
    subject = serializers.CharField(required=True)
    message = serializers.CharField(required=True)
    fullname = serializers.CharField(required=False)
    email = serializers.CharField(required=False)