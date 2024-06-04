from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User

from management_app.constants.choices_models import STATUS_CHOICES, PRIORITY_CHOICES


class Task(models.Model):
    name = models.CharField(max_length=120, unique=True, validators=[MinLengthValidator(10)])
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="new")
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES, default="Normal")
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    assignee = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='tasks',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Tasks'
        ordering = ['-due_date']
        unique_together = ('name', 'project')

    def __str__(self):
        return f"{self.name}, status: {self.status}"
