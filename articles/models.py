from django.db import models
from django.utils import timezone

# Create your models here.

import architect

@architect.install('partition', type='range', subtype='date', constraint='month', column='publish_time')
class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    publish_time = models.DateTimeField(default=timezone.now)
    update_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
      return self.title
