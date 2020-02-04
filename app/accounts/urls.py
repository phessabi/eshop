from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import CreateVendorViewSet, ListRetrieveVendorViewSet, UpdateRetrieveVendorViewSet, \
    CreateBuyerViewSet, UpdateRetrieveBuyerViewSet

router = routers.DefaultRouter()
router.register('vendor-registration', CreateVendorViewSet)
router.register('buyer-registration', CreateBuyerViewSet)
router.register('list-vendors', ListRetrieveVendorViewSet)
router.register('vendor-profile', UpdateRetrieveVendorViewSet)
router.register('buyer-profile', UpdateRetrieveBuyerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh')
]
