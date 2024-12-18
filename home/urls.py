from django.urls import path
from .views import TasksOverview, TaskActions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskActions, basename='task')


urlpatterns = [
    path("tasks/", TasksOverview.as_view(), name="tasks-overview"),
]

urlpatterns += router.urls
