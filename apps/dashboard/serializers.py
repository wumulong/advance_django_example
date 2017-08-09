from .models import Inventory
from rest_framework import serializers

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class InventorySerializer(serializers.ModelSerializer):
    ip = serializers.IPAddressField()
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tags = TagListSerializerField()

    class Meta:
        model = Inventory
        fields = ('id', 'name', 'ip', 'regions', 'create_time', 'update_time', 'tags')
