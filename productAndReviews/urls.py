from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import ProductViewSet, ReviewViewSet, ConatactMailViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('review', ReviewViewSet, basename='review')

urlpatterns = [
    path('', include(router.urls)),
    path('contactMail/', ConatactMailViewSet.as_view()),
]