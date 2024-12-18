from django.db import models
from accounts.models import User

# Create your models here.

class List(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    added_at = models.DateTimeField(auto_now_add=True)
    is_done = models.BooleanField(default=False)
    in_list = models.ForeignKey(List, on_delete=models.SET_NULL, null=True, blank=True)
    is_important = models.BooleanField(default=False)
