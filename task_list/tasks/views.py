from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskTable
from .serializers import TaskTableSerializer


class TaskTableView(APIView):
    def get(self, request):
        tasks = TaskTable.objects.filter(enabled=False)
        serializer = TaskTableSerializer(tasks, many=True)
        return Response(serializer.data)


class TaskTableDetailView(APIView):
    def get(self, request, pk):
        tasks = TaskTable.objects.get(id=pk, enabled=False)
        serializer = TaskTableSerializer(tasks)
        return Response(serializer.data)
