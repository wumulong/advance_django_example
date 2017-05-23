from article.models import Article
from rest_framework import serializers

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

class ArticleSerializer(serializers.ModelSerializer):
    publish_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    tags = TagListSerializerField()

    class Meta:
        model = User
        fields = ('id', 'title', 'author', 'tags', 'publish_time', 'update_time', 'content')
