from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'email', 'username', 'nickname', 'bio', 'url',
      'location', 'avatar')
