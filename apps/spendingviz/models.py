from django.db import models
from apps.core.models import TimestampedModel
from taggit.managers import TaggableManager


class Entry(TimestampedModel):
    cpi_index = models.IntegerField()
    cpi_text = models.CharField(max_length=20, blank=True, default='')
    amount = models.FloatField()
    note = models.TextField(blank=True, default='')
    tags = TaggableManager()

    def __str__(self):
        return self.note
