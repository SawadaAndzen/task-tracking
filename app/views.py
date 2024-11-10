from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm, CustomSignUpForm, TaskFilterForm
from .mixin import UserIsOwnerMixin


class TaskList(ListView):
    model = Task
    template_name = 'app/task_list.html'
    context_object_name = "tasks"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")
        
        if status:
            queryset = queryset.filter(status = status)
        if priority:
            queryset = queryset.filter(priority = priority)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context["filter_form"] = TaskFilterForm(self.request.GET)
        
        return context
    

class TaskDetail(DetailView):
    model = Task
    template_name = 'app/task_detail.html'
    context_object_name = "task"
    
    
class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = '/tasks/'
    template_name = 'app/task_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class TaskDelete(UserIsOwnerMixin, LoginRequiredMixin, DeleteView):
    model = Task
    success_url = "/"
    template_name = "app/confirm_delete.html"
    
    
class TaskUpdate(UserIsOwnerMixin, LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    login_url = "/login/"
    success_url = "/"
    template_name = "app/task_update.html"
    
    
class SignUp(CreateView):
    model = User
    form_class = CustomSignUpForm
    success_url = "/login/"
    template_name = "app/auth/signup.html"