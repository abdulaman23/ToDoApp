from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from django.core.cache import cache

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        cached_tasks = cache.get(f'tasks_{user_id}')
        if cached_tasks:
            return cached_tasks
        tasks = Task.objects.filter(user=self.request.user)
        cache.set(f'tasks_{user_id}', tasks, timeout=60*5)
        return tasks

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
