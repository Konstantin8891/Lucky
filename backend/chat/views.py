from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import ParseError
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView

from chat.filters import MessageFilter
from chat.models import Message
from chat.pagination import MessagePagination
from chat.serializers import MessageSerializer


class MessageView(ListAPIView):
    serializer_class = MessageSerializer
    pagination_class = MessagePagination
    filter_backends = (SearchFilter, DjangoFilterBackend)
    search_fields = ("title",)
    filterset_class = MessageFilter

    def get_queryset(self):
        user_id = self.request.GET.get("user_id")
        if not user_id:
            raise ParseError("Не передан user_id")
        return Message.objects.filter(chat__user__id=int(user_id)).order_by("-created_at")



