"""App serializers"""
from datetime import datetime
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from todo.models import Task


class TaskSerializer(ModelSerializer):
    """
    Task serializer

    Serialize all fields.
    """

    is_overdue = SerializerMethodField()

    class Meta:
        """Meta class"""

        model = Task
        fields = ["id", "title", "description", "done", "max_date", "is_overdue"]

    def get_is_overdue(self, obj: Task):
        """Returns if task is overdue"""
        return obj.max_date > datetime.now().date()
