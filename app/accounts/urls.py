from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views import CreateVendorViewSet
from accounts.views import ListRetrieveVendorViewSet
from accounts.views import UpdateRetrieveVendorViewSet

router = routers.DefaultRouter()
router.register('vendor-registration', CreateVendorViewSet)
router.register('list-vendors', ListRetrieveVendorViewSet)
router.register('vendor-profile', UpdateRetrieveVendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh')
]
