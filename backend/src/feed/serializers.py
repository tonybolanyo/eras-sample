from django.utils.translation import ugettext as _
from rest_framework import serializers

from .models import FeedItem

class FeedItemSerializer(serializers.ModelSerializer):
    """Default serializer for feed items."""

    class Meta:
        model = FeedItem
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')