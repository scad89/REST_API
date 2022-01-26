from .models import TaskTable
from .serializers import TaskTableSerializer
from rest_framework import viewsets, permissions
from .service import PaginationTasks


class TaskTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TaskTable.objects.all()
    pagination_class = PaginationTasks
#    permission_classes = [permissions.IsAuthenticated]   for Postman

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskTableSerializer
        elif self.action == "retrieve":
            return TaskTableSerializer
