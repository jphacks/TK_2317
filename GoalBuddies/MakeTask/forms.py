from django import forms
from .models import Task, Message

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'detail', 'duration', 'tags']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']