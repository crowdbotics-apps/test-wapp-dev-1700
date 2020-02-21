from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import OOOViewSet

router = DefaultRouter()
router.register("ooo", OOOViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
