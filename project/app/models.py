from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    date = models.DateTimeField(auto_now_add=True, blank=False)
    content = models.CharField(max_length=2000, blank=True)

    def __str__(self):
        return f'{self.title} - {self.date}'
