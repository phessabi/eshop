from django.urls import path, include
from rest_framework import routers

from products.views import ListProductViewSet, VendorProductViewSet, ListCategoryView, AdminCategoryViewSet

router = routers.DefaultRouter()
router.register('list-products', ListProductViewSet)
router.register('add-product', VendorProductViewSet, 'vendor-products')
router.register('list-categories', ListCategoryView)
router.register('admin-category', AdminCategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]
