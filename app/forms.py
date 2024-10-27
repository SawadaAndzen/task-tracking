from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority', 'deadline']
        widgets = {"deadline": forms.DateTimeInput(attrs = {'type': 'datetime-local'})}