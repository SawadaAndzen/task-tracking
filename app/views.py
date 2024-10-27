from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Task
from .forms import TaskForm


class TaskList(ListView):
    model = Task
    template_name = 'app/task_list.html'
    context_object_name = "tasks"
    

class TaskDetail(DetailView):
    model = Task
    template_name = 'app/task_detail.html'
    context_object_name = "task"
    
    
class TaskCreate(CreateView):
    model = Task
    form_class = TaskForm
    success_url = '/tasks/'
    template_name = 'app/task_create.html'