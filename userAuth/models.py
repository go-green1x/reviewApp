from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    upload = models.ImageField(upload_to ='uploads/profilepic/', blank = True, null=True)

    
    def __str__(self):
    	return '{}-{}'.format(self.user.first_name)   