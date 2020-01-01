from django.urls import path, include
from rest_framework import routers

from products.views import ListProductViewSet
from products.views import ProductCreateViewSet

router = routers.DefaultRouter()
router.register('list-products', ListProductViewSet)
router.register('add-product', ProductCreateViewSet)

urlpatterns = [
    path('', include(router.urls))
]
