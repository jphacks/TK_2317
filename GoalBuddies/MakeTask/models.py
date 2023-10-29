from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    TAG_CHOICES = [
        ('programming', 'プログラミング'),
        ('exam', '受験'),
        ('assignment', '課題'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    detail = models.TextField()
    duration = models.IntegerField()  # 日数で管理
    tags = models.CharField(max_length=50, choices=TAG_CHOICES)  # 選択肢で管理


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message by {self.sender.username} for task {self.task.name}'
    
class Match(models.Model):
    task1 = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='match_task1')
    task2 = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='match_task2')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Match between {self.task1.name} and {self.task2.name}'