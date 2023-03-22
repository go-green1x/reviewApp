from django.contrib import admin

from .models import Product, Review

# Register your models here.
models = [Product, Review]
admin.site.register(models)