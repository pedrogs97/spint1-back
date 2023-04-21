"""URL mappings for the Stock app"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from stock.views import MaterialViewSet

router = DefaultRouter()
router.register(
    "materials",
    MaterialViewSet,
)

app_name = "stock"

urlpatterns = [
    path("", include(router.urls)),
]
