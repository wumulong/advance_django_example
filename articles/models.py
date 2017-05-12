from django.db import models
from django.utils import timezone

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
      return self.title
