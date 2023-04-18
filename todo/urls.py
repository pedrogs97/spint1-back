"""URL mappings for the task app"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from todo.views import TaskViewSet

router = DefaultRouter()
router.register(
    "tasks",
    TaskViewSet,
)

app_name = "todo"

urlpatterns = [
    path("", include(router.urls)),
]
