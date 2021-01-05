from django.db import models
from django.contrib.auth import get_user_model

class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='task')

    def __str__(self):
        return self.title