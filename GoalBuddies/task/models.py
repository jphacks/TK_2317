from django.db import models
from model_utils.models import TimeStampedModel
from account.models import User

class Tag(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)

class Task(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    started_at = models.DateTimeField()
    ended_at = models.DateTimeField()
    tag = models.ForeignKey(Tag, on_delete=models.SET_NULL, null=True)
