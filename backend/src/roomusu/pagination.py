"""
Custom paginators for Django REST Framework
"""

from rest_framework.pagination import PageNumberPagination
from django.conf import settings


class DefaultPagination(PageNumberPagination):
    """
    Default pagination class for DRF using max elements by page.

    Max items per page can be passed as query param `page_size`.

    To configure this as default pagination method you should
    add to your settings as shown:

    ```
    # Pagination default settings
    PAGINATION_SETTINGS = {
        'DEFAULT_LIMIT': 50,
        'MAX_LIMIT_DEFAULT': 2000
    }
    ```
    """

    page_size = settings.PAGINATION_SETTINGS['DEFAULT_LIMIT']
    page_size_query_param = 'page_size'
    max_page_size = settings.PAGINATION_SETTINGS['MAX_LIMIT_DEFAULT']
