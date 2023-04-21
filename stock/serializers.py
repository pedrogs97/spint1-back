"""Serializer for app Stock"""
from rest_framework.serializers import ModelSerializer
from stock.models import Material


class MaterialSerializer(ModelSerializer):
    """
    Material serializer

    Serialize all fields.
    """

    class Meta:
        """Meta class"""

        model = Material
        fields = '__all__'
