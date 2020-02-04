from django.urls import path, include
from rest_framework import routers

from purchase.views import CartViewSet

router = routers.DefaultRouter()
router.register('cart', CartViewSet)

urlpatterns = [
    path('', include(router.urls))
]
