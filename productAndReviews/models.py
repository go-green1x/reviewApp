from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    average_cost = models.IntegerField()
    category = models.CharField(max_length=100)
    release_date = models.DateField()
    description = models.CharField(max_length=500)
    upload = models.ImageField(upload_to ='uploads/product/', blank = True, null=True)
    
    def __str__(self):
    	return '{}-{}'.format(self.name, self.manufacturer)   
    
class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.CharField(max_length=200)
    date_posted = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self):
    	return '{}-{}'.format(self.author, self.product)  