from rest_framework import serializers
from management_app.models import Task


class AllTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "name", "status", "priority")
