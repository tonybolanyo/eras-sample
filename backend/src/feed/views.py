from rest_framework.generics import ListAPIView

from .models import FeedItem
from .serializers import FeedItemSerializer


class FeedItemListView(ListAPIView):
    """List all items retrieved from external feed."""

    queryset = FeedItem.objects.all()
    serializer_class = FeedItemSerializer
    search_fields = ('title', 'city')
    ordering_fields = ('city', 'created', 'modified', 'title')
