from django.urls import path
from django.views.generic import TemplateView
from .views import TaskList, TaskDetail, TaskCreate, TaskDelete, TaskUpdate, CommentUpdate, CommentDelete, LikeCommentView, ProfileDetail, ProfileUpdate


urlpatterns = [
    path("tasks/", TaskList.as_view(), name = "task-list"),
    path("tasks/task/<int:pk>/", TaskDetail.as_view(), name = "task-detail"),
    path("tasks/create/", TaskCreate.as_view(), name = "task-create"),
    path("", TemplateView.as_view(template_name = "app/index.html"), name = "index"),
    path("tasks/delete/<int:pk>/", TaskDelete.as_view(), name = "task-delete"),
    path("tasks/update/<int:pk>/", TaskUpdate.as_view(), name = "task-update"),
    path("tasks/comments/delete/<int:pk>/", CommentDelete.as_view(), name = "comment-delete"),
    path("tasks/comments/update/<int:pk>/", CommentUpdate.as_view(), name = "comment-update"),
    path('comments/<int:comment_id>/like/', LikeCommentView.as_view(), name='like-comment'),
    path('profile/', ProfileDetail.as_view(), name = 'profile'),
    path('profile/update/', ProfileUpdate.as_view(), name = 'profile-update'),
]
