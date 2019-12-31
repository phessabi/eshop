from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from accounts.views.user import CreateUser

router = routers.DefaultRouter()
router.register('register', CreateUser)
router.register('token', TokenObtainPairView.as_view())
router.register('token/refresh', TokenRefreshView.as_view())

urlpatterns = [
    path('', include(router.urls)),
    # url(r'^token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url(r'^token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
