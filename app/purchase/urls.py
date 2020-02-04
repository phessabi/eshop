from django.urls import path, include
from rest_framework import routers

from purchase.views import CartViewSet, AddToCartView

router = routers.DefaultRouter()
router.register('cart', CartViewSet)
router.register('add-cart', AddToCartView)

urlpatterns = [
    path('', include(router.urls))
]
