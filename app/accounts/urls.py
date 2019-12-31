from django.urls import path, include
from rest_framework import routers

from accounts.views.vendor import CreateUser

router = routers.DefaultRouter()
router.register('register', CreateUser)

urlpatterns = [
    path('', include(router.urls))
]
