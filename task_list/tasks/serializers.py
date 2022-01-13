from rest_framework import serializers
from .models import TaskTable


class TaskTableSerializer(serializers.Serializer):
    class Meta:
        model = TaskTable
        fields = ('task_name', 'day_of_week', 'date',
                  'comment', 'id_user', 'enabled')
