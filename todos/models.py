from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    completed = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
