from django.urls import path, include
from rest_framework import routers

from purchase.views import CartViewSet, OrderViewSet, AddToCartView, DateView, PhoneAddressView, PaymentView, \
    CampaignViewSet

router = routers.DefaultRouter()
router.register('cart', CartViewSet)
router.register('add-cart', AddToCartView)
router.register('order', OrderViewSet)
router.register('phone-address', PhoneAddressView)
router.register('payment', PaymentView, basename='payment')
router.register('campaigns', CampaignViewSet, basename='campaigns')

urlpatterns = [
    path('date/', DateView.as_view(), name='date'),
    path('', include(router.urls)),
]
