from django.urls import path, include
from rest_framework import routers

from products.views import ListProductViewSet, VendorProductViewSet, ListCategoryView, AdminCategoryViewSet, ExpressView

router = routers.DefaultRouter()
router.register('list-products', ListProductViewSet)
router.register('vendor-product', VendorProductViewSet)
router.register('list-categories', ListCategoryView)
router.register('admin-category', AdminCategoryViewSet)
router.register('express', ExpressView)

urlpatterns = [
    path('', include(router.urls))
]
