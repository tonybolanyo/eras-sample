from django.core.management.base import BaseCommand, CommandError
from django.utils.translation import ugettext as _
from django.conf import settings
import urllib.request
import requests
import shutil
import json
from feed.models import FeedItem
import re
from babel.numbers import format_currency
import locale

locale.setlocale(locale.LC_ALL, '')

REG_EX = re.compile('[^a-zA-Z]')


class Command(BaseCommand):
    filename = 'feed.json'
    help = _('Download external JSON data file from spotahome feed')

    def handle(self, *args, **options):
        # # self.download()
        # self.import_data()
        print('Downloading...')
        headers = {'Content-Type': 'application/json'}
        response = requests.get(
            url=settings.FEED_URL,
            headers=headers,
        )
        response.raise_for_status()
        print('downloaded')
        data = response.json()
        print('get json data')
        for data_object in data:
            self.create_item(data_object)

    def download(self):
        try:
            url = settings.FEED_URL
            if not url:
                raise CommandError(
                    _('You should define FEED_URL in project settings file')
                )
            self.stdout.write(_('Downloading feed data...'))
            with urllib.request.urlopen(url) as feed, open(
                self.filename, 'wb'
            ) as out_file:
                data = feed.read()
                out_file.write(data)
            self.stdout.write(
                self.style.SUCCESS(_('Download finished succesfully'))
            )
        except:
            raise CommandError(
                _(f'Error while downloading external feed data from {url}')
            )

    def create_item(self, item):
        city = item.get('City', '').title()
        address = item.get('Address', '').title()
        images = item.get('Images', [])
        if images:
            image = images[0]
        else:
            image = None
        link = item.get('Link', '')
        deposit = item.get('Deposit', '')
        currency = item.get('Currency', 'EUR')
        start = link.find('for-rent:') + 9  # add 'for-rent:' length
        end = link.find('/', start) - 1  # remove last character (plural 's')
        item_type = REG_EX.sub('', link[start:end]).title()
        # assume link and deposit are mandatory
        price = format_currency(int(deposit), currency, locale='es_ES')
        title = f'{item_type} in {city} for {price}'

        try:
            feed_item, created = FeedItem.objects.get_or_create(
                title=title, link=link, address=address, city=city, image=image
            )
            if created:
                feed_item.save()
                print('.', end='', flush=True)
        except Exception as ex:
            print('E', end='', flush=True)
