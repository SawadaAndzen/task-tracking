from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Task, Comment


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'priority', 'deadline']
        widgets = {'deadline': forms.DateTimeInput(attrs = {'type': 'datetime-local', 'class': 'form-control'})}
        
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['status'].widget.attrs.update({'class': 'form-control'})
        self.fields['priority'].widget.attrs.update({'class': 'form-control'})
        
        
class CustomSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]
        
    def __init__(self, *args, **kwargs):
        super(CustomSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
 
 
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        
        
class TaskFilterForm(forms.Form):
    status_choices = [
        ("", "All"),
        ("_in_progress", 'In Progress'), 
        ("_done", "Done"), 
        ("_expired", "Expired")
    ]
    
    priority_choices = [
        ("", "All"),
        ("_low", "Low"), 
        ("_mid", "Middle"), 
        ("_high", "High")
    ]
    
    status = forms.ChoiceField(choices = status_choices, required = False, label = "Status",  widget = forms.Select(attrs={'class': 'form-control'}))
    priority = forms.ChoiceField(choices = priority_choices, required = False, label = "Priority", widget = forms.Select(attrs={'class': 'form-control'}))
    

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        labels = {'content': ''}
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 1,
                'cols': 50,
                'placeholder': 'Write your comment here...',
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)