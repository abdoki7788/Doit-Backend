from django.urls import path
from .views import TasksOverview

urlpatterns = [
    path("tasks/", TasksOverview.as_view(), name="tasks-overview")
]
