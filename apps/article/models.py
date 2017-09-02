from django.db import models
from django.conf import settings
from apps.core.models import TimestampedModel
from taggit.managers import TaggableManager


class Article(TimestampedModel):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.title
