from django.urls import path, include
from rest_framework import routers

from purchase.views import CartViewSet, AddCartViewSet

router = routers.DefaultRouter()
router.register('cart', CartViewSet)
router.register('add-cart', AddCartViewSet)

urlpatterns = [
    path('', include(router.urls))
]
