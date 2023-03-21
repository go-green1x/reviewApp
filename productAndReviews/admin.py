from django.contrib import admin

from .models import Product, Review, Info

# Register your models here.
models = [Product, Review, Info]
admin.site.register(models)