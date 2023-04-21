"""Views for Stock app"""
from drf_spectacular.utils import (
    extend_schema_view,
    extend_schema,
)
from rest_framework.viewsets import ModelViewSet
from stock.models import Material
from stock.serializers import MaterialSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Lista todos os itens em estoque.", description="Retorna todos os itens em estoque."
    ),
    retrieve=extend_schema(
        summary="Busca um material.", description="Retorna um material específico."
    ),
    create=extend_schema(summary="Novo  material.", description="Cria um novo material."),
    update=extend_schema(
        summary="Atuiliza um material.",
        description="Atualiza um material específico de forma completa completo."
    ),
    partial_update=extend_schema(
        summary="Atuiliza um material.",
        description="Atualiza um material específico de forma parcial."
    ),
    destroy=extend_schema(
        summary="Remove um material.", description="Remove um material específico."
    ),
)
class MaterialViewSet(ModelViewSet):
    """
    ViewSet for Material

    GET, POST, PUT, PATCH and DELETE
    """

    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
