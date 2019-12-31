from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views.vendor import CreateVendorViewSet

router = routers.DefaultRouter()
router.register('vendor-registration', CreateVendorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'^token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', TokenRefreshView.as_view(), name='token_refresh')
]
