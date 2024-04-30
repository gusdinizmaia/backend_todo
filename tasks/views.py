from .models import Task
from .serializers import TaskSerializer
from rest_framework import generics


class TaskView(generics.ListCreateAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    lookup_url_kwarg = "task_id"
