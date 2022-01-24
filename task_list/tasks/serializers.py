from rest_framework import serializers
from .models import TaskTable


class TaskTableSerializer(serializers.ModelSerializer):
    id_user = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = TaskTable
        exclude = ['enabled']
