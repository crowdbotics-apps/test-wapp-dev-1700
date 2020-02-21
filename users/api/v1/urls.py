from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OOOViewSet, UserViewSet

router = DefaultRouter()
router.register("ooo", OOOViewSet)
router.register("user", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
