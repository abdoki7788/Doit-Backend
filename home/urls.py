from django.urls import path
from .views import ListsActions, TasksOverview, TaskActions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tasks', TaskActions, basename='task')
router.register(r'lists', ListsActions, basename='list')


urlpatterns = [
    path("tasks/", TasksOverview.as_view(), name="tasks-overview"),
]

urlpatterns += router.urls
