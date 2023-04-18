"""Models for task model"""
from django.db import models


class Task(models.Model):
    """Task model"""

    id = models.BigIntegerField(primary_key=True, db_index=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True)
    done = models.BooleanField(default=False)
    max_date = models.DateField(null=True)

    objects = models.Manager()
