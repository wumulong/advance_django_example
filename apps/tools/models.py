import os

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

# Create your models here.


def upload_path(instance, filename):
    return os.path.join('upload', str(instance.owner.id), filename)


class Picture(models.Model):
    name = models.CharField(max_length=70, null=True, blank=True, default='')
    desc = models.CharField(max_length=70, null=True, blank=True, default='')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to=upload_path)
    pic_thumbnail = ImageSpecField(
        source='pic',
        format='JPEG',
        options={'quality': 70})
    tags = TaggableManager()

    def __str__(self):
        return self.name

