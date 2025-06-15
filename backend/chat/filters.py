from django_filters import CharFilter, FilterSet
from django.db.models import Q

from chat.models import Message


class MessageFilter(FilterSet):
    event = CharFilter(method="filter_event")

    class Meta:
        model = Message
        fields = ("event",)

    def filter_event(self, queryset, name, value):
        return queryset.filter(Q(event=value) | Q(event=Message.EventType.advertisement))
