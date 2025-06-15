from django.conf import settings
from rest_framework.pagination import PageNumberPagination


class MessagePagination(PageNumberPagination):
    """Пагинация консультации."""

    page_size = settings.MESSAGE_PAGE_SIZE
