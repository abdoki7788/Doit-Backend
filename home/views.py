from rest_framework import status
from rest_framework.generics    import RetrieveUpdateDestroyAPIView, mixins, ListCreateAPIView
from rest_framework.decorators  import action
from rest_framework.viewsets    import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response    import Response

from .models      import List, Task
from .serializers import TaskSerializer, ListSerializer

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

    def create(self, request, *args, **kwargs):
        s_data = self.serializer_class(data=request.data)
        s_data.is_valid(raise_exception=True)
        s_data.validated_data["author"] = request.user
        s_data.save()
        return Response(s_data.data, status=status.HTTP_201_CREATED)

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


class ListsActions(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = List.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ListSerializer

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

    @action(detail=False, methods=["get"])
    def add_list(self, request, *args, **kwargs):
        c_list = List.objects.create(author=request.user)
        s_data = self.serializer_class(instance=c_list)
        return Response(s_data.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=["post"], serializer_class=TaskSerializer)
    def add_task(self, request, *args, **kwargs):
        s_data = self.serializer_class(data=request.data)
        s_data.is_valid(raise_exception=True)
        s_data.validated_data["in_list"] = self.get_object()
        s_data.validated_data["author"] = request.user
        s_data.save()
        return Response(s_data.data, status=status.HTTP_201_CREATED)
