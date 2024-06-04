from django.contrib.auth.password_validation import MinimumLengthValidator
from django.db import models

from management_app.models.constants import STATUS_CHOICES


class Task(models.Model):
    name = models.CharField(max_length=120, unique=True, validators=MinimumLengthValidator(min_length=10))
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
