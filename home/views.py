from rest_framework             import generics
from rest_framework.permissions import IsAuthenticated

from .models      import Task
from .serializers import TaskSerializer

# Create your views here.

class TasksOverview(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)
