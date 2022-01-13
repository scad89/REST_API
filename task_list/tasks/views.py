from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TaskTable
from .serializers import TaskTableSerializer


class TaskTableView(APIView):
    def get(self, request):
        tasks = TaskTable.objects.filter(enabled=False)
        serializer = TaskTableSerializer(tasks, many=True)
        return Response(serializer.data)
