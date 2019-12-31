from django.urls import path, include
from rest_framework import routers

from products.views.product_list import ListProductViewSet

router = routers.DefaultRouter()
router.register('list', ListProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
