from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import TaskTable
from .serializers import TaskTableSerializer


class TaskTableViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = TaskTable.objects.all()
        serializer = TaskTableSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TaskTable.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskTableSerializer(task)
        return Response(serializer.data)
