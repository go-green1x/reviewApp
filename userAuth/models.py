from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.core.files.storage import DefaultStorage

class OverwriteStorage(DefaultStorage):
    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            self.delete(name)
        return name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    upload = models.ImageField(upload_to ='uploads/profilepic/', blank = True, null=True, storage=OverwriteStorage())

    
    def __str__(self):
    	return '{}-{}'.format(self.user.first_name)   