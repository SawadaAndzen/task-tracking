from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Comment, Like
from .forms import TaskForm, CustomSignUpForm, TaskFilterForm, CommentForm
from .mixin import UserIsOwnerMixin, UserIsCommentOwnerMixin


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = self.object.comment_set.all()
        context["comments_form"] = CommentForm
        context["current_user"] = self.request.user
        
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit = False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.created_at = timezone.now()
            
            comment.save()
            
            return redirect("task-detail", pk = self.get_object().id)
    
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
    login_url = "/login/"
    template_name = "app/confirm_delete.html"
    
    
class TaskUpdate(UserIsOwnerMixin, LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    login_url = "/login/"
    success_url = "/"
    template_name = "app/task_update.html"
    
    
class CommentUpdate(LoginRequiredMixin, UserIsCommentOwnerMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    success_url = "/"
    login_url = "/login/"
    template_name = "app/comment_update.html"
    
    def get_success_url(self):
        return reverse_lazy("task-detail", kwargs = {"pk" : self.get_object().task.pk})
    
    
class CommentDelete(LoginRequiredMixin, UserIsCommentOwnerMixin, DeleteView):
    model = Comment
    success_url = "/"
    login_url = "/login/"
    template_name = "app/confirm_delete.html"
    
    def get_success_url(self):
        return reverse_lazy("task-detail", kwargs = {"pk" : self.get_object().task.pk})
    
    
class LikeCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)

        like, created = Like.objects.get_or_create(user=request.user, comment=comment)
        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        total_likes = comment.likes.count()
        return JsonResponse({'liked': liked, 'total_likes': total_likes})
    
    
class SignUp(CreateView):
    model = User
    form_class = CustomSignUpForm
    success_url = "/login/"
    template_name = "app/auth/signup.html"