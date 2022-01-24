from .models import TaskTable
from .serializers import TaskTableSerializer
from rest_framework import generics


class TaskTableView(generics.ListAPIView):
    serializer_class = TaskTableSerializer

    def get_queryset(self):
        tasks = TaskTable.objects.filter(enabled=False)
        return tasks


class TaskTableDetailView(generics.RetrieveAPIView):
    queryset = TaskTable.objects.filter(enabled=False)
    serializer_class = TaskTableSerializer
