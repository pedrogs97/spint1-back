"""Views for task app"""
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from rest_framework.viewsets import ModelViewSet
from todo.models import Task
from todo.serializers import TaskSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Lista todas as tarefas.", description="Retorna todas as tarefas."
    ),
    retrieve=extend_schema(
        summary="Tarefa específica.", description="Retorna uma tarefas específica."
    ),
    create=extend_schema(summary="Nova tarefa.", description="Cria uma nova tarefa."),
    update=extend_schema(
        summary="Atuilizada uma tarefa.", description="Atualiza uma tarefa específica."
    ),
    partial_update=extend_schema(
        summary="Atuilizada uma tarefa.", description="Atualiza uma tarefa específica."
    ),
    destroy=extend_schema(
        summary="Remove uma tarefa.", description="Remove uma tarefa específica."
    ),
)
class TaskViewSet(ModelViewSet):
    """
    ViewSet for Task

    GET, POST, PUT, PATCH and DELETE
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
