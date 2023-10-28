from django.db import models
from model_utils.models import TimeStampedModel
from account.models import User
from task.models import Task, Tag

class Message(TimeStampedModel):
    content = models.TextField()

class Match(TimeStampedModel):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1_matches')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2_matches')
    task1 = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task1_matches')
    task2 = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task2_matches')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
