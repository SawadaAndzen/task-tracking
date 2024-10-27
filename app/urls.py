from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate


urlpatterns = [
    path("tasks/", TaskList.as_view(), name = "task-list"),
    path("tasks/task/<int:pk>/", TaskDetail.as_view(), name = "task-detail"),
    path("tasks/create/", TaskCreate.as_view(), name = "task-create")
]
