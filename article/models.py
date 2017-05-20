from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
      return self.title
