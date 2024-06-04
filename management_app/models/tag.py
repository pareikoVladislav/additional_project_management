from django.db import models

from management_app.models import Task


class Tag(models.Model):
    name = models.CharField(max_length=70, unique=True)
    tasks = models.ManyToManyField(Task, related_name='tags')
