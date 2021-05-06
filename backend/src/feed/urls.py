from django.urls import include, path

from .views import FeedItemListView

urlpatterns = [path('', FeedItemListView.as_view())]
