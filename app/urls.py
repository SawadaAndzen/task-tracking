from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from .views import TaskList, TaskDetail, TaskCreate, TaskDelete, TaskUpdate, SignUp


urlpatterns = [
    path("tasks/", TaskList.as_view(), name = "task-list"),
    path("tasks/task/<int:pk>/", TaskDetail.as_view(), name = "task-detail"),
    path("tasks/create/", TaskCreate.as_view(), name = "task-create"),
    path("", TemplateView.as_view(template_name = "app/index.html"), name = "index"),
    path("tasks/delete/<int:pk>/", TaskDelete.as_view(), name = "task-delete"),
    path("tasks/update/<int:pk>/", TaskUpdate.as_view(), name = "task-update"),
]
