from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from taggit.managers import TaggableManager

# Create your models here.


class Inventory(models.Model):
    name = models.CharField(max_length=70, null=True, blank=True, default='')
    ip = models.GenericIPAddressField(unpack_ipv4=True, unique=True)
    regions = models.CharField(max_length=70, null=True, blank=True, default='')
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    ssh_port = models.CharField(max_length=5, default='22')
    root_password = models.CharField(max_length=255)
    root_password_key = models.CharField(max_length=255)
    tags = TaggableManager()

    def __str__(self):
        return self.name

    def clean(self):
        if not self.ip:
            raise ValidationError({'ip': '请输入 IP！'})
        elif not self.root_password:
            raise ValidationError({'ip': '请输入 root 密码！'})
        if self.ip:
            i = Inventory.objects.filter(ip=self.ip)
            if i:
                raise ValidationError({'ip': '相同 IP 的资产已经存在！'})
