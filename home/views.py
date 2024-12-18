from rest_framework.generics    import mixins, ListCreateAPIView
from rest_framework.decorators  import action
from rest_framework.viewsets    import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response

from .models      import Task
from .serializers import TaskSerializer

# Create your views here.

class TasksOverview(ListCreateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)


class TaskActions(mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    @action(detail=True, methods=["get"])
    def set_done(self, request, pk):
        obj = self.get_object()
        obj.is_done = not obj.is_done
        obj.save()
        return Response(self.serializer_class(obj).data)
    
    @action(detail=True, methods=["get"])
    def add_important(self, request, pk):
        obj = self.get_object()
        obj.is_important = not obj.is_important
        obj.save()
        return Response(self.serializer_class(obj).data)
    
    @action(detail=False, methods=["get"])
    def importants(self, request):
        queryset = self.get_queryset().filter(is_important=True)
        return Response(self.serializer_class(queryset, many=True).data)
