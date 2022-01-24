from .models import TaskTable
from .serializers import TaskTableSerializer
from rest_framework import viewsets
from rest_framework import generics


class TaskTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskTable.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskTableSerializer
        elif self.action == "retrieve":
            return TaskTableSerializer
