from rest_framework import serializers
from management_app.models import Tag


class AllTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'name')
