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
    image = models.ImageField(upload_to = "tasks-media/", blank = True, null = True)
    media = models.FileField(upload_to = "tasks-media/", blank = True, null = True)
    
    def __str__(self):
        return f"{self.name} by {self.user.username}"
    
    
class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    content = models.TextField()
    media = models.FileField(upload_to = "comments-media/", blank = True, null = True)
    created_at = models.DateTimeField()

    def __str__(self):
        return f"Comment by {self.author} for the task: {self.task}"
    
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete = models.CASCADE, related_name = 'likes')
    
    class Meta:
        unique_together = ('user', 'comment')
        
    def __str__(self):
        return f'{self.comment} liked by {self.user}'
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.FileField(upload_to="profile-media/", blank=True, null=True)
    
    def __str__(self):
        return self.user.username