from django.urls import path, include
from rest_framework import routers

from products.views.product import ListRetrieveProductViewSet

router = routers.DefaultRouter()
router.register('list', ListRetrieveProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
