from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField()
    status = models.CharField(max_length = 12, choices = [
        ("_in_progress", 'In Progress'), ("_done", "Done"), ("_expired", "Expired")
    ])
    priority = models.CharField(max_length = 6, choices = [
        ("_low", "Low"), ("_mid", "Middle"), ("_high", "High")
    ])
    deadline = models.DateTimeField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)