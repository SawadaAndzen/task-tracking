from django.contrib import admin
from .models import Task, Comment, Profile, Like

admin.site.register(Task)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Like)