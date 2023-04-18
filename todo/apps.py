"""Configuration for task app"""
from django.apps import AppConfig


class TodoConfig(AppConfig):
    """Default config for task app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "todo"
