from django.db import models
from django.utils.translation import ugettext as _
from django_extensions.db.models import TimeStampedModel


class FeedItem(TimeStampedModel, models.Model):
    """Items loaded from external JSON feed file."""

    title = models.CharField(_('title'), max_length=500, db_index=True)
    link = models.URLField(_('link'), max_length=255)
    address = models.TextField(_('address'), db_index=True)
    city = models.CharField(_('city'), max_length=100, db_index=True)
    image = models.CharField(_('image'), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('feed item')
        verbose_name_plural = _('feed items')
        ordering = ('pk',)
        get_latest_by = 'modified'
