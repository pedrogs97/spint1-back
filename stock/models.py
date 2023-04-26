"""Model of app Stock"""
from django.db import models


class Material(models.Model):
    """Material model"""

    id = models.BigAutoField(primary_key=True, db_index=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    observation = models.CharField(max_length=150, blank=True)
    quantity = models.PositiveSmallIntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    last_replacement = models.DateField(null=True)
    updated_at = models.DateField(auto_now=True)

    objects = models.Manager()
